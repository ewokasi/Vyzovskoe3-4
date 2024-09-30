import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense
from pickle import dump, load
from datetime import datetime

def get_raw_filtered_train_test_and_val_data():
    sheet = pd.read_csv('V8.csv')
    filtered_sheet  = sheet[['depth_of_tree', 'profit_markup']]
    filtered_sheet["profit"] = sheet['profit']

    sheet_x = filtered_sheet.iloc[:,:2]
    sheet_y= filtered_sheet['profit']#profit index in headers oh filtering stage

    seed =7
    test_size = 0.2
    val_size = 0.25
    x_train, x_test, y_train, y_test = train_test_split(sheet_x, sheet_y, test_size = test_size, random_state = seed)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = val_size, random_state = seed)
    return x_train, y_train, x_test, y_test, x_val, y_val 

if __name__ =="__main__":
    with open('rmm_teaching_predictions.txt', 'w') as output_file:
                    output_file.write(f"{datetime.now()}\n")

    x_train, y_train, x_test, y_test, x_val, y_val = get_raw_filtered_train_test_and_val_data()
    print(x_train)

    model = Sequential()
    model.add(SimpleRNN(400, activation='relu', input_shape=(x_train.shape[1], 1)))
    model.add(Dense(1))  # Выходной слой

    model.compile(optimizer='adam', loss='mean_squared_error')

    # Обучение модели
    model.fit(x_train, y_train, epochs=400, batch_size=32, validation_data=(x_val, y_val))

    # Прогнозирование
    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    # Оценка модели
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    r2_train = r2_score(y_train, y_train_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    r2_test = r2_score(y_test, y_test_pred)
    
    with open('rmm_teaching_predictions.txt', 'a') as output_file:
        output_file.write(f"Train RMSE: {rmse_train}\n")
        output_file.write(f"Train R2 Score: {r2_train}\n")
        output_file.write(f"Test RMSE: {rmse_test}\n")
        output_file.write(f"Test R2 Score: {r2_test}\n")
        output_file.write(f"#######################\n")

    
    with open('rmm_teaching_predictions.txt', 'a') as f:
        f.write(f"actual, predicted\n")
        for actual, predicted in zip(y_test, y_test_pred):
            f.write(f"{actual}, {predicted[0]} \n")


    filename = '400_epochs_RMM__Raw_Filtered_data.sav'
    dump(model, open(filename, 'wb'))
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
import os
from datetime import datetime
sheet = pd.read_csv('V8.csv')
filtered_sheet  = sheet
filtered_sheet['cost_price'].fillna(3500, inplace=True)

sheet_x = filtered_sheet.iloc[:,:6]
sheet_y= filtered_sheet['profit']#profit index in headers oh filtering stage

bestfeatures = SelectKBest(f_regression, k=3)
fit = bestfeatures.fit(sheet_x, sheet_y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(sheet_x.columns)
featureScores = pd.concat([dfcolumns, dfscores], axis =1)
print(featureScores)
filtered_sheet  = sheet[['depth_of_tree', 'profit_markup']]
filtered_sheet["profit"] = sheet['profit']

def get_raw_train_test_and_val_data():
    sheet = pd.read_csv('V8.csv')
    filtered_sheet  = sheet
    filtered_sheet['cost_price'].fillna(3500, inplace=True)

    sheet_x = filtered_sheet.iloc[:,:6]
    sheet_y= filtered_sheet['profit']#profit index in headers oh filtering stage

    seed =7
    test_size = 0.2
    val_size = 0.25
    x_train, x_test, y_train, y_test = train_test_split(sheet_x, sheet_y, test_size = test_size, random_state = seed)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = val_size, random_state = seed)
    return x_train, y_train, x_test, y_test, x_val, y_val 


def get_normalized_train_test_and_val_data():
    sheet = pd.read_csv('V8.csv')
    filtered_sheet  = sheet
    filtered_sheet['cost_price'].fillna(3500, inplace=True)

    #Нормализация
    scaler = Normalizer().fit(filtered_sheet)
    rescaled_sheet = pd.DataFrame(scaler.fit_transform(filtered_sheet))
    rescaled_sheet = rescaled_sheet.rename(columns={0:'Unnamed: 0', 1:"cost_price", 2:'profit_markup', 3: "3",
                                                    4:"depth_of_tree", 5:"sales_commission", 6:"profit"})
    #print(rescaled_sheet)

    #раделение наборов на тренировочный и тестовый и проверочный
    sheet_x = rescaled_sheet.iloc[:,:6]
    sheet_y= rescaled_sheet['profit']#profit index in headers oh filtering stage

    seed =7
    test_size = 0.2
    val_size = 0.25
    x_train, x_test, y_train, y_test = train_test_split(sheet_x, sheet_y, test_size = test_size, random_state = seed)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = val_size, random_state = seed)

    return x_train, y_train, x_test, y_test, x_val, y_val 

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



def get_normalized_filtered_train_test_and_val_data():
    sheet = pd.read_csv('V8.csv')
    filtered_sheet  = sheet[['depth_of_tree', 'profit_markup']]
    #filtered_sheet["type_to_depth_rel"] = sheet['profit_markup']/sheet["depth_of_tree"]
    filtered_sheet["profit"] = sheet['profit']

    #Нормализация
    scaler = Normalizer().fit(filtered_sheet)
    rescaled_sheet = pd.DataFrame(scaler.fit_transform(filtered_sheet))
    rescaled_sheet = rescaled_sheet.rename(columns={0:'depth_of_tree', 1:"profit_markup", 2:'profit'})
    #print(rescaled_sheet)

    #раделение наборов на тренировочный и тестовый и проверочный
    sheet_x = rescaled_sheet.iloc[:,:2]
    sheet_y= rescaled_sheet['profit']#profit index in headers oh filtering stage

    seed =7
    test_size = 0.2
    val_size = 0.25
    x_train, x_test, y_train, y_test = train_test_split(sheet_x, sheet_y, test_size = test_size, random_state = seed)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = val_size, random_state = seed)

    return x_train, y_train, x_test, y_test, x_val, y_val 


for data_function in [
    get_normalized_filtered_train_test_and_val_data,
    get_normalized_train_test_and_val_data,
    get_raw_filtered_train_test_and_val_data,
    get_raw_train_test_and_val_data]:

    x_train, y_train, x_test, y_test, x_val, y_val = data_function()
    model = Sequential()
    model.add(SimpleRNN(150, activation='relu', input_shape=(x_train.shape[1], 1)))
    model.add(Dense(1))  # Выходной слой

    model.compile(optimizer='adam', loss='mean_squared_error')

    # Обучение модели
    model.fit(x_train, y_train, epochs=100, batch_size=32, validation_data=(x_val, y_val))

    # Прогнозирование
    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)
    y_val_pred = model.predict(x_val)

    # Оценка модели
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    r2_train = r2_score(y_train, y_train_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    r2_test = r2_score(y_test, y_test_pred)
    rmse_val = np.sqrt(mean_squared_error(y_val, y_val_pred))
    r2_val = r2_score(y_val, y_val_pred)
    
    with open('output.txt', 'a+') as output_file:
        output_file.write(f"Data function: {data_function.__name__}\n")
        output_file.write(f"Train RMSE for RMM: {rmse_train}\n")
        output_file.write(f"Train R2 Score for RMM: {r2_train}\n")
        output_file.write(f"Test RMSE for RMM: {rmse_test}\n")
        output_file.write(f"Test R2 Score for RMM: {r2_test}\n")
        output_file.write(f"Valid RMSE for RMM: {rmse_val}\n")
        output_file.write(f"Valid R2 Score for RMM: {r2_val}\n")

        


    model = LinearRegression()
    model.fit(x_train, y_train)

    y_prediction = model.predict(x_train)
    y_test_pred = model.predict(x_test)
    y_val_pred = model.predict(x_val)
        # Оценка модели
    rmse_train = np.sqrt(mean_squared_error(y_train, y_prediction))
    r2_train = r2_score(y_train, y_train_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    r2_test = r2_score(y_test, y_test_pred)
    rmse_val = np.sqrt(mean_squared_error(y_val, y_val_pred))
    r2_val = r2_score(y_val, y_val_pred)

    
    with open('output.txt', 'a+') as output_file:
        output_file.write('\n')
        output_file.write(f"Data function: {data_function.__name__}\n")
        output_file.write(f"Train RMSE for LIN: {rmse_train}\n")
        output_file.write(f"Train R2 Score for LIN: {r2_train}\n")
        output_file.write(f"Test RMSE for LIN: {rmse_test}\n")
        output_file.write(f"Test R2 Score for LIN: {r2_test}\n")
        output_file.write(f"Valid RMSE for LIN: {rmse_val}\n")
        output_file.write(f"Valid R2 Score for LIN: {r2_val}\n\n")
        output_file.write("#################################\n\n")

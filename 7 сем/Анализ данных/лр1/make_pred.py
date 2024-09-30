from joblib import load
import numpy as np


model = load('400_epochs_RMM__Raw_Filtered_data.sav')

x = np.array([[6, 5]])  #Сначала depth_of_tree, затем profit_markup

y_pred = model.predict(x)

print(y_pred)

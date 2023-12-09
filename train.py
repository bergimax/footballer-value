#!/usr/bin/env python
# coding: utf-8

#imports
import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor

#Loading data
df = pd.read_csv('data/player_data.csv')

#Standardize the col name:
df.columns = df.columns.str.lower().str.replace(" ", "_")
strings = list(df.dtypes[df.dtypes == 'object'].index) #ottengo gli indici che hanno solo valori string

for col in strings: #loop per ogni colonna
    df[col] = df[col].str.lower().str.replace(" ", "_") 

#Delete some columns
del df['winger']
del df['position_encoded']
del df['player']

#setting the logatitm value
player_val = ['current_value', 'highest_value']
for v in player_val: #loop per ogni colonna
    df[v] = np.log1p(df[v])

#splitting the dataset
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=11)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=11)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)

#setting the target variable
y_train = df_train.current_value
y_val = df_val.current_value
y_test = df_test.current_value
y_full_train = df_full_train.current_value


#deliting the target column from the dataset
del df_train['current_value']
del df_val['current_value']
del df_test['current_value']
del df_full_train['current_value']

#define the metrics
def rmse(y, y_pred):
    error = y - y_pred #calcolo errore tra i 2 array
    se = error **2 #quadrato della differenza
    mse = se.mean() #media della differenza
    return np.sqrt(mse) #radice del valore medio


# Random Forest  

#train
train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)
#val
val_dicts = df_val.to_dict(orient='records')
X_val = dv.transform(val_dicts)
#ft
#train
dicts_ft = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse = False)
X_full_train = dv.fit_transform(dicts_ft)
#test
dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)

model = RandomForestRegressor(n_estimators=60, 
                           max_depth= 20,
                           min_samples_leaf=5,
                           random_state=1)
model.fit(X_full_train, y_full_train)
#predict
dicts_test = df_test.to_dict(orient='records')
   
X_test = dv.transform(dicts_test)
y_pred = model.predict(X_test)

_rmse = rmse(y_test, y_pred)


print('rmse: ', _rmse)

output_file = 'player_model.bin'
with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)
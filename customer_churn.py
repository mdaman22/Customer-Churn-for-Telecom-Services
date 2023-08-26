# -*- coding: utf-8 -*-
"""Customer_Churn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kdHMtvi3VSWclojhQ9OvZlIybsAuYu7R
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Data = pd.read_csv("/content/customer_churn.csv")

Data

Data.info()

Data['Churn'].value_counts()

Data['Churn'] = pd.get_dummies(Data['Churn'], drop_first = True )

Data

Data.info()

# Data['TotalCharges'] = Data['TotalCharges'].astype('float64')
Data['TotalCharges'] = Data.TotalCharges.replace(" ",'0').astype(float)

Data['Churn'] = Data['Churn'].astype('int64')

Data.info()

X = Data[['SeniorCitizen','tenure','MonthlyCharges']]

X

y = Data.iloc[:,-1]

y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size = 0.75, random_state = 42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LogisticRegression

model1 = LogisticRegression()
model1.fit(X_train,y_train)
y_pred = model1.predict(X_test)
y_pred

Data

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,y_pred))

sns.heatmap(confusion_matrix(y_test,y_pred), annot = True, fmt=".2f")
plt.show()

confusion_matrix(y_test,y_pred)


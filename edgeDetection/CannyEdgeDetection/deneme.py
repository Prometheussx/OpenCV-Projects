# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:32:35 2022

@author: erdem
"""

"""
Created on Sat Jul  7 00:47:02 2018
@author: user
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("multiple-linear-regression-dataset.csv",sep = ";")

x = df.iloc[:,[0,2]].values
y = df.Salary.values.reshape(-1,1)

# %% fitting data
multiple_linear_regression = LinearRegression()
multiple_linear_regression.fit(x,y)

print("b0: ", multiple_linear_regression.intercept_)
print("b1,b2: ",multiple_linear_regression.coef_)

# predict
multiple_linear_regression.predict(np.array([[10,35],[5,35]]))
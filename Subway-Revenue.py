import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

from Dividing_Function import MonthRevenue as MR

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', header=0, usecols=[3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 36])
# print(Subway)
Revenue = MR

Subway = np.array(Subway).reshape(-1, 2)
# print(len(Subway))
# print(Subway)
Revenue = np.array(Revenue).reshape(-1, 1)
# print(len(Revenue))

train_i, test_i, train_o, test_o = tts(Subway, Revenue, test_size=0.5, random_state=42)

lr = LR()
lr.fit(train_i, train_o)

print(lr.score(train_i, train_o))
print(lr.score(test_i, test_o))

A = lr.predict([[17910424, 2472165]])
print(A / 1000000)
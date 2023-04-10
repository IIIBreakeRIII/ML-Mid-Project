import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

from Dividing_Function_Revenue import MonthRevenue as MR
from Dividing_Function_Loss import MonthLoss as ML

MR = np.array(MR).reshape(-1, 2)
ML = np.array(ML).reshape(-1, 2)

print(len(MR))
print(len(ML))

poly = PF(degree=2, include_bias=False)
poly.fit(MR)
train_poly = poly.transform(MR)

train_input, test_input, train_output, test_output = tts(train_poly, ML, test_size=0.2, random_state=42)

lr = LR()
lr.fit(train_input, train_output)

print(lr.score(train_input, train_output))
print(lr.score(test_input, test_output))


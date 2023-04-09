import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', index_col=0, header=0, usecols=[3, 4])
# print(Subway)
Revenue = pd.read_excel('Data/All_Revenue_Loss.xlsx', index_col=0, header=0)

Subway = np.array(Subway)
Revenue = np.array(Revenue)

# 데이터 확인
print(len(Subway))
print(len(Revenue))

# plt.plot(Subway)
# plt.plot(Revenue)
# plt.show()

poly = PF(degree=3, include_bias=False)
poly.fit(Subway)
train_poly = poly.transform(Subway)

testSize = 0.1

for i in range(9):
  train_i, test_i, train_o, test_o = tts(train_poly, Revenue, test_size=testSize, random_state=42)

  lr = LR()
  lr.fit(train_i, train_o)

  print("test_size =", testSize, " =", lr.score(train_i, train_o))
  print("test_size =", testSize, " =", lr.score(test_i, test_o))

  testSize = testSize + 0.1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

from Dividing_Function_Revenue import MonthRevenue as MR

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', header=0, usecols=[3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 36])
# print(Subway)
Revenue = MR

Subway = np.array(Subway).reshape(-1, 2)
# print(len(Subway))
# print(Subway)
Revenue = np.array(Revenue).reshape(-1, 1)
# print(len(Revenue))
# print(Revenue)

poly = PF(degree=2, include_bias=False)
poly.fit(Subway)
train_poly = poly.transform(Subway)

train_input, test_input, train_target, test_target = tts(train_poly, Revenue, test_size=0.1, random_state=42)

lr = LR()
lr.fit(train_input, train_target)
# lr.predict()

print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))

coef = lr.coef_
intercept = lr.intercept_

predictValue = 22955000
predictValue2 = 3082293

sum = 0

for i in range(9):
  if i == 0:
    sum = sum + (coef[0][0] * predictValue)
  elif i == 1:
    sum = sum + (coef[0][1] * predictValue2)
  elif i == 2:
    sum = sum + (coef[0][2] * predictValue ** 2)
  elif i == 3:
    sum = sum + (coef[0][3] * predictValue * predictValue2)
  elif i == 4:
    sum = sum + (coef[0][4] * predictValue2 ** 2)
  elif i == 5:
    sum = sum + (coef[0][5] * predictValue ** 3)
  elif i == 6:
    sum = sum + (coef[0][6] * predictValue ** 2 * predictValue2)
  elif i == 7:
    sum = sum + (coef[0][7] * predictValue * predictValue2 ** 2)
  elif i == 8:
    sum = sum + (coef[0][8] * predictValue2 ** 3)

sum = sum + intercept[0]

print(sum)

# print(train_poly.shape)
# print(poly.get_feature_names_out())

# degree = 2
# print((4.19297300e+02 * predictValue) + (5.50221259e+03 * predictValue2) + (-2.28294629e-06 * predictValue ** 2) + 
#       (1.45129121e-04 * predictValue * predictValue2) + (-1.45776247e-03 * predictValue2 ** 2) - 3.6967415e+09)

# degree = 3
# print((-1.18065469e-08 * predictValue) + (4.52430337e-10 * predictValue2) + (3.13676462e-05 * predictValue ** 2) +
#       (-2.66575320e-04 * predictValue * predictValue2) + (2.49046843e-03 * predictValue2 ** 2) + (-7.19109243e-13 * predictValue ** 3) +
#       (7.39187418e-12 * predictValue ** 2 * predictValue2) + (2.92105437e-11 * predictValue * predictValue2 ** 2) + 
#       (-5.95931553e-10 * predictValue2 ** 3) + 4.07018285e+09)



# [[-1.18065469e-08  4.52430337e-10  3.13676462e-05 -2.66575320e-04
#    2.49046843e-03 -7.19109243e-13  7.39187418e-12  2.92105437e-11
#   -5.95931553e-10]] [4.07018285e+09]

# ['x0' 'x1' 'x0^2' 'x0 x1' 'x1^2' 'x0^3' 'x0^2 x1' 'x0 x1^2' 'x1^3']

print(1.71863505e+10)
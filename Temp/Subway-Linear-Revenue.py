## 선형회귀 개같이 멸망


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

train_i, test_i, train_o, test_o = tts(Subway, Revenue, test_size=0.2, random_state=42)

lr = LR()
lr.fit(train_i, train_o)

plt.scatter(train_i[:, 0], train_o[:, 0])
plt.scatter(28493000, 22286000000, marker='^')
plt.show()

print(lr.score(train_i, train_o))
print(lr.score(test_i, test_o))

A = lr.predict([[28493000, 3932872]])
B = lr.predict([[31023000, 3707533]])
C = lr.predict([[13695000, 1895215]])
print(B)

print(lr.coef_, lr.intercept_)



# print((13.3977 * 13916000 ** 5) + (17.9566 * 13916000 ** 4) + (-12.2057 * 13916000 ** 3) + (-0.0550 * 13916000 ** 2) + (-6.9626 * 13916000) - 1.0488)

# 13916000
# 13.3976823131  17.9565644997  -12.2056914155    -0.05498147605   -6.96260923241 ] [-1.04878524396]
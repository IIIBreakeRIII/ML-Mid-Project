import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR

from Dividing_Function_Loss import MonthLoss as ML

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', header=0, usecols=[4, 8, 12, 16, 20, 24, 28, 32, 36])
Loss = ML

Subway = np.array(Subway).reshape(-1, 1)
print(Subway)
Loss = np.array(Loss).reshape(-1, 1)

plt.plot(Subway)
plt.show()
plt.plot(Loss)
plt.show()

train_i, test_i, train_o, test_o = tts(Subway, Loss, test_size=0.5, random_state=42)

lr = LR()
lr.fit(train_i, train_o)

print(lr.score(train_i, train_o))
print(lr.score(test_i, test_o))
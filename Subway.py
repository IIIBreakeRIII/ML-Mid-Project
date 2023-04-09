import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

from Population import PopulationInfo as PI
from Population import AllPopulation as AP

AllSubway = pd.read_excel('Data/Subway_Old_Final.xlsx', index_col=0, header=0)
AllSubway = AllSubway.drop(['Line1-People', 'Line1-Old', 'Line1-People-All'], axis = 1)
AllSubway = AllSubway.drop(['Line2-People', 'Line2-Old', 'Line2-People-All', 'Line2-Old-Exchange'], axis = 1)
AllSubway = AllSubway.drop(['Line3-People', 'Line3-Old', 'Line3-People-All', 'Line3-Old-Exchange'], axis = 1)
AllSubway = AllSubway.drop(['Line4-People', 'Line4-Old', 'Line4-People-All', 'Line4-Old-Exchange'], axis = 1)
AllSubway = AllSubway.drop(['Line5-People', 'Line5-Old', 'Line5-People-All', 'Line5-Old-Exchange'], axis = 1)
AllSubway = AllSubway.drop(['Line6-People', 'Line6-Old', 'Line6-People-All', 'Line6-Old-Exchange'], axis = 1)
AllSubway = AllSubway.drop(['Line7-People', 'Line7-Old', 'Line7-People-All', 'Line7-Old-Exchange'], axis = 1)
AllSubway = AllSubway.drop(['Line8-People', 'Line8-Old', 'Line8-People-All', 'Line8-Old-Exchange'], axis = 1)
AllSubway = AllSubway.drop(['Line9-People', 'Line9-Old', 'Line9-People-All', 'Line9-Old-Exchange'], axis = 1)

AllSubway = np.array(AllSubway)

poly = PF(degree=3, include_bias=False)
poly.fit(AP)
train_poly = poly.transform(AP)

train_i, test_i, train_o, test_o = tts(train_poly, AllSubway, random_state=42)

lr = LR()
lr.fit(train_i, train_o)

print(lr.score(train_i, train_o))
print(lr.score(test_i, test_o))
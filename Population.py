import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

AllPopulation = pd.read_excel('Data/All_Population.xlsx', index_col=0, header=0)

# 전체 인구수 삭제
AllPopulation = AllPopulation.drop(AllPopulation.index[0])

# 2010년부터 2017년까지 삭제
AllPopulation = AllPopulation.drop(['2010S', '2010K', '2011S', '2011K', '2012S', '2012K',
                                    '2013S', '2013K', '2014S', '2014K', '2015S', '2015K',
                                    '2016S', '2016K', '2017S', '2017K'], axis=1)

PopulationInfo = []
temp = []

# 2018
SY = KY = SO = KO = YSum = OSum = 0

for i2018 in range(65):
  SY = SY + AllPopulation.loc[i2018, '2018S']
  KY = KY + AllPopulation.loc[i2018, '2018K']
  YSum = SY + KY
  
for j2018 in range(65, 101):
  SO = SO + AllPopulation.loc[j2018, "2018S"]
  KO = KO + AllPopulation.loc[j2018, "2018K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2019
SY = KY = SO = KO = YSum = OSum = 0

for i2019 in range(65):
  SY = SY + AllPopulation.loc[i2019, '2019S']
  KY = KY + AllPopulation.loc[i2019, '2019K']
  YSum = SY + KY
  
for j2019 in range(65, 101):
  SO = SO + AllPopulation.loc[j2019, "2019S"]
  KO = KO + AllPopulation.loc[j2019, "2019K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2020
SY = KY = SO = KO = YSum = OSum = 0

for i2020 in range(65):
  SY = SY + AllPopulation.loc[i2020, '2020S']
  KY = KY + AllPopulation.loc[i2020, '2020K']
  YSum = SY + KY
  
for j2020 in range(65, 101):
  SO = SO + AllPopulation.loc[j2020, "2020S"]
  KO = KO + AllPopulation.loc[j2020, "2020K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2021
SY = KY = SO = KO = YSum = OSum = 0

for i2021 in range(65):
  SY = SY + AllPopulation.loc[i2021, '2021S']
  KY = KY + AllPopulation.loc[i2021, '2021K']
  YSum = SY + KY
  
for j2021 in range(65, 101):
  SO = SO + AllPopulation.loc[j2021, "2021S"]
  KO = KO + AllPopulation.loc[j2021, "2021K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# # 2022
# SY = KY = SO = KO = YSum = OSum = 0

# for i2022 in range(65):
#   SY = SY + AllPopulation.loc[i2022, '2022S']
#   KY = KY + AllPopulation.loc[i2022, '2022K']
#   YSum = SY + KY
  
# for j2022 in range(65, 101):
#   SO = SO + AllPopulation.loc[j2022, "2022S"]
#   KO = KO + AllPopulation.loc[j2022, "2022K"]
#   OSum = SO + KO

# temp.append(YSum)
# temp.append(OSum)
# PopulationInfo.append(temp)
# temp = []
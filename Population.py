import pandas as pd

# index_col = 특정 열 인덱스 지정
# header = 행의 제목
AllPopulation = pd.read_excel('Data/All_Population.xlsx', index_col=0, header=0)

# AllPopulation.index[0] => 첫번째 행 삭제
AllPopulation = AllPopulation.drop(AllPopulation.index[0])

PopulationInfo = []
temp = []

# 2010
SY = KY = SO = KO = YSum = OSum = 0

for i2010 in range(65):
  SY = SY + AllPopulation.loc[i2010, '2010S']
  KY = KY + AllPopulation.loc[i2010, '2010K']
  YSum = SY + KY
  
for j2010 in range(65, 101):
  SO = SO + AllPopulation.loc[j2010, "2010S"]
  KO = KO + AllPopulation.loc[j2010, "2010K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp =[]

# 2011
SY = KY = SO = KO = YSum = OSum = 0

for i2011 in range(65):
  SY = SY + AllPopulation.loc[i2011, '2011S']
  KY = KY + AllPopulation.loc[i2011, '2011K']
  YSum = SY + KY
  
for j2011 in range(65, 101):
  SO = SO + AllPopulation.loc[j2011, "2011S"]
  KO = KO + AllPopulation.loc[j2011, "2011K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2012
SY = KY = SO = KO = YSum = OSum = 0

for i2012 in range(65):
  SY = SY + AllPopulation.loc[i2012, '2012S']
  KY = KY + AllPopulation.loc[i2012, '2012K']
  YSum = SY + KY
  
for j2012 in range(65, 101):
  SO = SO + AllPopulation.loc[j2012, "2012S"]
  KO = KO + AllPopulation.loc[j2012, "2012K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2013
SY = KY = SO = KO = YSum = OSum = 0

for i2013 in range(65):
  SY = SY + AllPopulation.loc[i2013, '2013S']
  KY = KY + AllPopulation.loc[i2013, '2013K']
  YSum = SY + KY
  
for j2013 in range(65, 101):
  SO = SO + AllPopulation.loc[j2013, "2013S"]
  KO = KO + AllPopulation.loc[j2013, "2013K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2014
SY = KY = SO = KO = YSum = OSum = 0

for i2014 in range(65):
  SY = SY + AllPopulation.loc[i2014, '2014S']
  KY = KY + AllPopulation.loc[i2014, '2014K']
  YSum = SY + KY
  
for j2014 in range(65, 101):
  SO = SO + AllPopulation.loc[j2014, "2014S"]
  KO = KO + AllPopulation.loc[j2014, "2014K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2015
SY = KY = SO = KO = YSum = OSum = 0

for i2015 in range(65):
  SY = SY + AllPopulation.loc[i2015, '2015S']
  KY = KY + AllPopulation.loc[i2015, '2015K']
  YSum = SY + KY
  
for j2015 in range(65, 101):
  SO = SO + AllPopulation.loc[j2015, "2015S"]
  KO = KO + AllPopulation.loc[j2015, "2015K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2016
SY = KY = SO = KO = YSum = OSum = 0

for i2016 in range(65):
  SY = SY + AllPopulation.loc[i2016, '2016S']
  KY = KY + AllPopulation.loc[i2016, '2016K']
  YSum = SY + KY
  
for j2016 in range(65, 101):
  SO = SO + AllPopulation.loc[j2016, "2016S"]
  KO = KO + AllPopulation.loc[j2016, "2016K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []

# 2017
SY = KY = SO = KO = YSum = OSum = 0

for i2017 in range(65):
  SY = SY + AllPopulation.loc[i2017, '2017S']
  KY = KY + AllPopulation.loc[i2017, '2017K']
  YSum = SY + KY
  
for j2017 in range(65, 101):
  SO = SO + AllPopulation.loc[j2017, "2017S"]
  KO = KO + AllPopulation.loc[j2017, "2017K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
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

# 2022
SY = KY = SO = KO = YSum = OSum = 0

for i2022 in range(65):
  SY = SY + AllPopulation.loc[i2022, '2022S']
  KY = KY + AllPopulation.loc[i2022, '2022K']
  YSum = SY + KY
  
for j2022 in range(65, 101):
  SO = SO + AllPopulation.loc[j2022, "2022S"]
  KO = KO + AllPopulation.loc[j2022, "2022K"]
  OSum = SO + KO

temp.append(YSum)
temp.append(OSum)
PopulationInfo.append(temp)
temp = []
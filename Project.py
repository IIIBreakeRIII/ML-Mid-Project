import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# index_col = 특정 열 인덱스 지정
# header = 행의 제목
AllPopulation = pd.read_excel('Data/All_Population.xlsx', index_col=0, header=0)
AllSubway = pd.read_excel('Data/All_Subway.xlsx')

# AllPopulation.index[0] => 첫번째 행 삭제
AllPopulation = AllPopulation.drop(AllPopulation.index[0])
AllPopulation = AllPopulation.loc[:, '2010S':'2010K']

# print(AllPopulation)

AllPopulation.plot()
plt.show()

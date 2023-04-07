import pandas as pd
import matplotlib.pyplot as plt

AllSubway = pd.read_excel('Data/All_Subway.xlsx', index_col=0, header=0, usecols=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

print(AllSubway)

AllSubway.plot()
plt.show()
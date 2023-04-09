import matplotlib.pyplot as plt
import pandas as pd

from PopulationTest import PopulationInfo as PI

RateList = []

for i in range(len(PI)):
  rate = PI[i][1] / PI[i][0]
  RateList.append(rate)

RateListPlot = pd.DataFrame(RateList)
RateListPlot.plot()
plt.show()
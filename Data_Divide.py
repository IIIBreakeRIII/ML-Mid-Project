import pandas as pd

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', index_col=0, header=0)
Revenue = pd.read_excel('Data/All_Revenue_Loss.xlsx', index_col=0, header=0)

# Subway 셀에서 호선별 전체 이용자 수
# 1 ~ 9호선
index = [2, 6, 10, 14, 18, 22, 26, 30, 34]

# 매월 호선별 전체 이용자 수 합 리스트
MonthPeople = []

# MonthPeople을 구하기 위한 식
for i in index:
  SumPeople = 0
  SumPeople = Subway.iloc[0, i] // 1000
  MonthPeople.append(SumPeople)

# 비율 계산
AllMonthPeople = 0
for i in range(9):
  AllMonthPeople = AllMonthPeople + MonthPeople[i]

ratio = []
for i in range(9):
  temp = 0
  temp = MonthPeople[i] / AllMonthPeople
  ratio.append(temp)

# 각 노선별 2018년 1월 전체 이용자 대비 수익
MonthRevenue = []

# Revenue.iloc[0, 0] = 각각 행, 열을 의미
for i in range(9):
  Revenue2018 = 0
  Revenue2018 = Revenue.iloc[0, 0] * ratio[i]
  MonthRevenue.append(Revenue2018)
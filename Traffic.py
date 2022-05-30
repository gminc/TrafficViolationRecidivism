import math
import pandas as pd
import numpy as np
import statistics as st
from collections import Counter

# 讀取 csv 檔案: 111-03台北市交通違規累犯
csvData = pd.read_csv(
    r'C:\Users\user\Downloads\111-03交通違規累犯.csv', usecols=[1, 2, 3])

# 直接讀取 pandas DataFrame, 用和 SQL 類似語句查詢
print(csvData.info())
print(str('\n') + str('80歲無照駕駛累犯資料'))
print(csvData[(csvData['年齡'] == 80) & (csvData['違規態樣'] == '無照駕駛累犯')])
print(str('\n') + str('18歲以下無照駕駛累犯年齡個數'))
print(csvData[csvData['違規態樣'] == '18歲以下無照駕駛累犯'].groupby(['年齡']).size())
print(str('\n') + str('20 歲的違規樣態種類和個數'))
print(csvData[csvData['年齡'] == 20].groupby(['違規態樣']).size())

# 資料切片
topFiveDataRow = csvData[:5]
print(str('\n取得前五筆資料'))
print(topFiveDataRow)

# 依欄位名稱取資料並轉成 list
allList = csvData.values.tolist()
ageList = list(csvData.loc[:, '年齡'])
genderList = list(csvData.loc[:, '違規人性別'])
violationList = list(csvData.loc[:, '違規態樣'])

# 移除 nan


def removeNan(list):
    count = len(list) - 1
    while count != 0:
        if math.isnan(list[count]):
            del list[count]
        count = count - 1


removeNan(ageList)

# 取得年齡相關基本資料:
# 中位數
median = '交通違規累犯{0}中位數: {1}'
print(str('\n') + median.format(('年齡'), str(st.median(ageList))))
# 平均數
print(str('交通違規累犯年齡平均數: ') + str(round(st.mean(ageList), 1)) + str('\n'))
# 年齡分布區間
ageArea = '{0:-5} 到 {1} 歲 累犯人數: {2}'
startAge = 0
endAge = 10
while startAge != 80:
    print(ageArea.format(startAge, endAge, sum(
        i in range(startAge, endAge) for i in ageList)))
    startAge = startAge + 10
    endAge = endAge + 10
print('{0:-7} 以上　 累犯人數: {1}'.format(startAge, sum(i > startAge for i in ageList)) + str('\n'))

# 統計資料


def GetUniqueAmount(uniqueList, allDataList, dataName):
    string = dataName + ': {0} \t 總數: {1}'
    for i in uniqueList:
        print(string.format(i, allDataList.count(i)))
    print()


# 取得性別統計資料
GetUniqueAmount(Counter(genderList).keys(), genderList, '性別')

# 取得違規種類統計資料
GetUniqueAmount(Counter(violationList).keys(), violationList, '違規種類')

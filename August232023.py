import pandas as pd
import numpy as np
#
# df = pd.DataFrame([[1, np.nan, 2],
#                    [2, 3, 5],
#                    [np.nan, 4, 6]])
# print('------------Printing dataFrame with Nan-------------')
# print(df)
# print('------------Printing dataFrame after dropna -------------')
# d1 = df.dropna()
# print(d1)
# print('------------Printing dataFrame after dropna with column axis-------------')
# d2 = df.dropna(axis="columns")
# print(d2)
# print('------------Printing dataFrame after dropna with rows axis(which is default) -------------')
# d3 = df.dropna(axis="rows")
# print(d3)
# print('------------Printing dropna with how(any=if NaN found, remove that -------------')
# d4 = df.dropna(axis='columns', how="any")
# print(d4)
# print('------------Printing dropna with how(all= if all NaN found,only then remove that -------------')
# d5 = df.dropna(axis='columns', how="all")
# print(d5)
# print('------------Printing dropna with thresh imply, minimum x no of Nan so that it is printed -------------')
# d6 = df.dropna(axis='columns', thresh=2)
# print(d6)
# print('------------Printing filna-------------')
# d7=df.fillna(45,axis='columns')
# print(d7)

dataFrame=pd.read_csv("Building_Permits.csv",low_memory=False)
print('\n---------DataFrame--------\n')
print(dataFrame)
print('\n---------DataFrame Info--------\n')
print(dataFrame.info)
print('---------DataFrame head but converted to string--------')
print(dataFrame.head().to_string())
print('---------DataFrame columns only--------')
print(dataFrame.columns)
print('---------DataFrame Analaysis--------')
dataShape=dataFrame.shape
print(f'The shape of dataFrame is {dataShape}')
totalCells=np.prod(dataShape)
print(f'The total number of cells is {totalCells}')
missingColumn=np.sum(dataFrame.isnull())
print(f'The total missing data in each column is :{missingColumn}')
totalMissingData=np.sum(missingColumn)
#Conceptually, columns act as its explicit index,so it sums the values only//
print(f'Total missing data across all columns is {totalMissingData}')
percentOfMissData=totalMissingData/totalCells*100
print(f'The percent of missing data is {percentOfMissData}%')
# missingColumnSeries=pd.Series(missingColumn)
# x=missingColumnSeries['Street Number Suffix']
# print( f'The percent of street number missing is:{x/dataShape[0]*100}%')
#Numpy and pandas are interchangeable
y=missingColumn[['Street Number Suffix','Street Suffix']]
print(y)
print( f'The percent of street number missing is:{y/dataShape[0]*100}%')

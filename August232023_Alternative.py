import pandas as pd
import numpy as np

dataFrame = pd.read_csv('Building_Permits.csv',low_memory=False)
# print(dataFrame.info)
# print(dataFrame.head().to_string())
# print(dataFrame.columns)

dataShape = dataFrame.shape
print(dataShape)

totalCells= np.prod(dataShape)
print(f'Total Cells {totalCells}')

mssingDataPerColumn = np.sum(dataFrame.isnull())
print(mssingDataPerColumn)

##FIND TOTAL MISSING DATA ACROSS ALL COLUMNS
totalMissingData = np.sum(mssingDataPerColumn)
print(totalMissingData)

missingPercentage = (totalMissingData/totalCells)*100
print(missingPercentage)

      ###USE SIMILAR ANALYSIS FOR STREET NUMBER SUFFIX AND ZIPCODE
print("=========")
missingDataColumn = mssingDataPerColumn[['Street Number Suffix','Zipcode']]
print(missingDataColumn)

percentageSNS = (missingDataColumn[0]/dataShape[0])*100
print(percentageSNS)

percentageZip = (missingDataColumn[1]/dataShape[0])*100
print(percentageZip)
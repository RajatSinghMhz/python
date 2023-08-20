import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt
import seaborn as sns
sns.set()
dataFrame=pd.read_csv("Seattle2014.csv")
print(dataFrame)
print('-----------------------')
precipitationData=dataFrame["PRCP"]
pptArray=np.array(precipitationData)
print(pptArray)
print('--------------------------')

#No of days with no rainfall
print(np.sum(pptArray==0))
#No of days with max rainfall
print(np.sum(pptArray==(np.max(pptArray))))
#No of days with more than 100mm rainfall
print(np.sum(pptArray>100))
#No of days with 10-100 rainfall
print(np.sum((pptArray>10) & (pptArray<100)))


#August17 Part
#Rainydays data print
print(f' Rainy day data is: {pptArray[pptArray>0]}')

#Median rainfall on rainy days
print(f'Median rainfall on rainy days is: {np.median(pptArray[pptArray>0])}')
#Maximum rainfall on rainy days
print(f'Maximum rainfall on rainy days is: {np.max(pptArray[pptArray>0])}')
#minimum rainfall on rainy days
print(f'Minimum rainfall on rainy days is: {np.min(pptArray[pptArray>0])}')
#min rainfall on summer days
days=np.arange(365)
summerDays=(days>172) & (days<262)
#Using Boolean masking concept
print(f'Minimum rainfall on summerdays is: {np.min(pptArray[summerDays])}')
#min ranfall on no summer days
print(f'Minimum rainfall on no summerdays is: {np.min(pptArray[~summerDays])}')


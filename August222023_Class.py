import pandas as pd
import numpy as np
#Pandas important function
print("\n-------------------------Reading a csv--------------------------------------------------------\n")
dataFrame=pd.read_csv('KathmanduHouse.csv')
print(dataFrame)
print("\n-------------------------Viewing Data:(Head and tail by default gives 5 data)-------------------\n")
print(dataFrame.head())
print("\n-------------------------Passing parameter to head returns the number of rows-----------------------\n")
print(dataFrame.head(10))
print("\n-------------------------Tail-------------------------------------------------------------------------\n")
print(dataFrame.tail())
print("\n--------------------------Sample----------------------------------------------------------------------\n")
print(dataFrame.sample(10))
print('\n----------------------------Info-------------------------------------------------------------------------\n')
print(dataFrame.info())
print('\n----------------------------Columns-------------------------------------------------------------------------\n')
print(dataFrame.columns)
print('\n----------------------------Check if null/ Find null/ Print not nulls----------------------------------------\n')
x=pd.Series([1,2,3,4,np.nan,None])
print(x.isnull())
print('\n')
print(np.sum(x.isnull()))
print('\n')
print(x[x.isnull()])
print('\n')
print(x[x.notnull()])
print('\n')
print('\n----------------------------Removing null values------------------------------------------------------------\n')
y=x.dropna()
print('For dropna')
print(f"Y value is {y}")
print(f"X value is {x}")
y=x.dropna(replace=True)
print('For dropna Replace True')
print(f"Y value is {y}")
print(f"X value is {x}")
z=x.fillna(45)
print('For fillna Replace True')
print(f"Y value is {z}")
print(f"X value is {x}")

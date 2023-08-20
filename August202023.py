import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Use of pandas
'''
1. Data cleaning
2. Data insights
3. Data formatting

Types:

1. Pandas Series=== Just a column single dimension columns.// Takes multiple datatypes unlike numpy which takes only single dataType.
2. Dataframe=== Dictionary like object with rows and columns.
'''
print('======================== Series Making ===============================')
mySeries = pd.Series([1, 2, 3, 4, 5, "6Six", True])
print(mySeries)
print(mySeries[5])
print(mySeries.values)
print(mySeries.index)

#Note: Doesn't take negative indexing unlike numPy or lists

print('=======================  Explicit Indexing ================================')
myNewSeries=pd.Series([1,2,3,4,5],index=['a','b','c','d','c'])
print(myNewSeries)
print(myNewSeries.index)
print(myNewSeries["c"])
print(myNewSeries["c"].index)
print(myNewSeries["c"][0])
#Index doesn't need to be unique unlike in dictionary
#If index repeats, then it forms array, else it forms value only

print('=======================  Assigning index from panda series ================================')
studentMarks=pd.Series([100,120,131,99,97])
studentRoll=pd.Series([1,3,5,7,9])
studentMarks.index=studentRoll
print(studentRoll.is_unique)
print(studentMarks[5])

print('======================= Assigning index from dictionary ================================')
dobDictionary={
    "sahil":'Aug/04/1998',
    'meow':'Jun/29/1998',
    'woof':'Feb/04/1998'
}
personDob=pd.Series(dobDictionary)
print(personDob.values)
print(personDob.index)

print('======================= Creating data frame fro Dictionary ================================')
dataFrame=pd.DataFrame([
    {'a':100,'b':200},
    {'c':300,'d':400},
    {'a':100,'b':200}
])
print(dataFrame)
# print(f'The date of birth of {name} is: {personDOB[name]}')
print('======================= Examples ================================')
area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995
             }

population_dict = {'California': 3833251,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135
                   }
areaSeries=pd.Series(area_dict)
populationSeries=pd.Series(population_dict)

stateFrame=pd.DataFrame({'Area':areaSeries,'Population':populationSeries})
#This takes multidimensional array or multidimensional dictionary or combination of both
print(stateFrame)
print('----------------------------')
print(stateFrame['Population'])
print('----------------------------')
stateFrame["Density"]=stateFrame['Population']/stateFrame['Area']
print(stateFrame)
print('----------------------------')
print(stateFrame.columns)
print('----------------------------')
print(stateFrame.head(1))
print('----------------------------')
print(stateFrame.iloc[:3,:2])
print('----------------------------')
print(stateFrame.loc[:'Florida',:'Area'])
print('----------------------------')

print('======================= Why loc or iloc needed ================================')
data=pd.Series(['a','b','c'],index=[1,3,5])
print(f'Printing using explicit index: {data[1]}')
print(f'Printing using explicit index: \n{data[1:3]}')
#But error happens when explicit index=implict index in large data set, so iloc or loc used
print("Using loc")
print(data.loc[1])
print(data.loc[1:3])
#Explicit uses loc// so 1 and 3 taken
print('Using iloc')
print(data.iloc[1])
print(data.iloc[1:3])
#implicit uses iloc// so 1 and 2 taken

print('======================= Index ================================')
index=pd.Index([1,2,3,4])
print(index)
print(index.ndim)
print(index.dtype)
print(index.size)
print(index.shape)
# index[1]=1
# print(index)
# #Index is immutable

print('======================= Index properties ================================')
indA = pd.Index([1, 2, 3, 4, 5, 6, 9])
indB = pd.Index([2, 3, 5, 7, 12, 34, 56, 90])
print(indA & indB)
print(indA | indB)
print(indA ^ indB)

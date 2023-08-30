import pandas as pd
import numpy as np

myBookDataFrame = pd.read_csv('BL-Flickr-Images-Book.csv')

print(myBookDataFrame.columns)
print('-------------------------------------------------')
###WORKs
#1 : Remove unnecessary Columns
columnsToDrop = ['Edition Statement','Contributors','Corporate Author',
    'Corporate Contributors','Former owner','Engraver','Issuance type','Shelfmarks']
myBookDataFrame.drop(columns=columnsToDrop,inplace=True)
print("After Dropping")
print(myBookDataFrame.columns)
#2 : Find column that is unique
#2.1 : Find if the unique column has null values
remainingColumns = myBookDataFrame.columns
nullandUniqueColumns = []
for col in remainingColumns:
    if(myBookDataFrame[col].is_unique and
             np.sum(myBookDataFrame[col].isnull()) == 0):
        nullandUniqueColumns.append(col)

print("NUll and Unique Columns")
print(nullandUniqueColumns)

#3 :change the index to ISBN or Identifiesr
print("==========")
myBookDataFrame.set_index('Identifier',inplace=True)
print(myBookDataFrame.index)
print(myBookDataFrame.loc[206])

#4: Columns to appropriate data types
print("=====================")
print(myBookDataFrame.info)
print("====================")
print(myBookDataFrame.dtypes)
print("---------------------")
print(myBookDataFrame.sample(10).to_string())
print("----------Using Regex----------------")

regex = r'(\d{4})'
dateOfPublication = myBookDataFrame['Date of Publication'];
satisfiedData = dateOfPublication.str.extract(regex,expand=False)
print(type(satisfiedData))

print("=========")
myBookDataFrame["Date of Publication"] = pd.to_numeric(satisfiedData)
print(myBookDataFrame.dtypes)

print("-----------------------------")
nullValues = np.sum(myBookDataFrame['Date of Publication'].isnull())
print("Percentage of Null Values",nullValues)
print(nullValues/len(myBookDataFrame['Date of Publication']))
#################
placeOfPublication = myBookDataFrame['Place of Publication']
print(placeOfPublication.loc[157633])

london = placeOfPublication.str.contains('London')
oxford = placeOfPublication.str.contains('Oxford')
# print(london)
# print(oxford)

print("Issues Data")
print(myBookDataFrame.loc[4157862])
print(myBookDataFrame.loc[4159587])
#np.where(cond,True,Flas)
myBookDataFrame['Place of Publication'] = np.where(london,'London',
                                                   np.where(oxford,'Oxford',
                                                            placeOfPublication.str.replace('-',' ')))
print(myBookDataFrame['Place of Publication'].sample(10))


print(myBookDataFrame.loc[4157862])
print(myBookDataFrame.loc[4159587])
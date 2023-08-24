import pandas as pd
import numpy as np
print('\n--------------Reading content from file--------------\n')
filepath=r'university_towns.txt'
file=open(filepath,'r')
fileData=file.readlines()
print(fileData)
print('\n-------------Extracting data from file into list as tuple pair---------------\n')
universityData=[]
for line in fileData:
    if "[edit]" in line:
        uniValue=line
    else:
        universityData.append((uniValue,line))
print(universityData)
print('\n--------------Making Dataframe from TUPLE--------------\n')
universityDataFrame=pd.DataFrame(universityData,columns=['State','Location'])
print(universityDataFrame)
print('\n--------------Defining a filtering function--------------\n')

'''
Question: Does applymap send data in reverse column order? the function call doesn't work when "[" used before "("

def removeUnwanted(stateLocUni):
    if "[" in stateLocUni:
        return stateLocUni[:stateLocUni.find("[")]
    elif "(" in stateLocUni:
        return stateLocUni[:stateLocUni.find(" (")]
    else:
        return stateLocUni
'''
def removeUnwanted(stateLocUni):
    if "(" in stateLocUni:
        return stateLocUni[:stateLocUni.find(" (")]
    elif "[" in stateLocUni:
        return stateLocUni[:stateLocUni.find("[")]
    else:
        return stateLocUni
def universityFinder(uniOnly):
    if "(" in uniOnly:
        return uniOnly[uniOnly.find("("):uniOnly.find(")")+1]
    else:
        return 0
print('\n--------------Applying map to filter required contents--------------\n')
universityFilteredDataFrame=universityDataFrame.applymap(removeUnwanted)
print(universityFilteredDataFrame)
print('\n--------------Applying new map filter to extract university as it used "(" parameter as Location--------------\n')
universitySeries=universityDataFrame.applymap(universityFinder)
print(universitySeries)
print('\n--------------Assigning DataFrame to DataFrame so using column Indexing as applymap copies default column format to dataFrame--------------\n')
universityFilteredDataFrame['University']=universitySeries['Location']
print(universityFilteredDataFrame)



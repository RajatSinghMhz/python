import pandas as pd
import numpy as np
dobMonth={
    '101':'1',
    '102':'12',
    '103':'11',
    '104':'09'
}
dobYear={
    '101':'1996',
    '102':'1998',
    '103':'1996',
    '104':'1997'
}
dobDay={
    '101':'1',
    '102':'2',
    '103':'10',
    '104':'23'
}
marks={
    '101':50,
    '102':90,
    '103':30,
    '104':15
}
graceMarks={
    '101':5,
    '102':90,
    '103':15,
    '104':10
}
print('-------------Extracting data from dictionary into Panda Column Series---------------')
dobDaySeries=pd.Series(dobDay)
dobMonthSeries=pd.Series(dobMonth)
dobYearSeries=pd.Series(dobYear)
marksSeries=pd.Series(marks)
graceMarksSeries=pd.Series(graceMarks)
# for mar in marksSeries:
#     testMarkSeries=marksSeries+graceMarksSeries
# newArray=np.array(testMarkSeries)
# print(newArray[newArray>40])
print('-------------Extracting data from Panda Column Series into Panda DataFrame// Concatenate,add,subtract,divide can be done here---------------')
dataFrame=pd.DataFrame({'Day':dobDaySeries,'Month':dobMonthSeries,'Year':dobYearSeries,"Full Date":dobYearSeries+"/"+dobMonthSeries+"/"+dobDaySeries,'Marks Obtained':marksSeries,'Grace Marks':graceMarksSeries,'Total Marks':marksSeries+graceMarksSeries})
# dataFrame['Result']=dataFrame['Total Marks']>40
print("-------------Defining a function to return pass or fail------------")
def passFailFunction(value):
    if (value>40):
     return "Pass"
    else:
     return "Fail"
print("---------Defining a new Panda Column Series using map function and taking input from defined function-------")
newArray=pd.Series(map(lambda x: passFailFunction(x),dataFrame['Total Marks']))
print('----------Since new series defined doesnt have same index as other series, matching index first----------')
newArray.index=graceMarksSeries.index
print('----------Once index are matched, we can directly add new column in dataframe like this---------')
dataFrame['Result']=newArray
# dataFrame[')Result']=dataFrame['Total Marks'].apply(lambda x: passFailFunction(x))
print(dataFrame)
print('-------This is used to export file to excel----------')
dataFrame.to_csv('August222023Export.csv',index=False)
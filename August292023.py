import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
euro12=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")
print(euro12)
print("\n-------------------------------------------------------------------\n")
print(euro12.head())
print("\n-------------------------------------------------------------------\n")
euroGoals=euro12["Goals"]
print(euroGoals)
print("\n-------------------------------------------------------------------\n")
print("Participated Team")
print(euro12.shape[0])
print("\n-------------------------------------------------------------------\n")
print("Number of Columns")
print(euro12.shape[1])
print("\n-------------------------------------------------------------------\n")
columnsToExtract=["Yellow Cards","Red Cards","Team"]
discipline=euro12[columnsToExtract]
print(discipline)
print("\n-------------------------------------------------------------------\n")
discipline=discipline.sort_values(['Red Cards','Yellow Cards'],ascending=False)
print(discipline)
print("\n-------------------------------------------------------------------\n")
print(f"Mean Yellow Card {np.mean(euro12['Yellow Cards'])}")
print("\n-------------------------------------------------------------------\n")
print("Team Scoring more than 6 goals")
print([euro12["Goals"]>4])
print(euro12[euro12["Goals"]>4])
print("\n-------------------------------------------------------------------\n")
print("Tem Starting with G")
regexStartingWithG=r'^G'
print(euro12[euro12["Team"].str.match(regexStartingWithG)])
print("\n-------------------------------------------------------------------\n")
print("first 7 columns")
print(euro12.iloc[:,:7].to_string())
print("\n-------------------------------------------------------------------\n")
print("Select all columns except last 3")
print(euro12.iloc[:,:-3].to_string())

print("Shooting accuracy from england, russia and italy")
myData=euro12["Team"].isin(["England","Italy","Russia"])
print(myData)
print("\n-------------------------------------------------------------------\n")
shootingAccuracyAndTeam=euro12.loc[euro12['Team'].isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]
print(shootingAccuracyAndTeam)
print("\n-------------------------------------------------------------------\n")
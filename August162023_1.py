import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()

# Reading a csv File
dataFrame = pd.read_csv('president_heights.csv')
print(dataFrame)

# Extracting file from row
print(dataFrame.iloc[2])

# Extracting File from Column
print(dataFrame['height(cm)'])
name=np.array(dataFrame['name'])

height = np.array(dataFrame['height(cm)'])
print(height)
# print tallest president
print(f'Tallest president is {np.max(height)}')
print(f"The tallest president is {name[height==np.max(height)]}")
# print Smallest President
print(f'Tallest president is {np.min(height)}')
# Print average height
print(f'Average:{np.mean(height)}')
# Median height
print(f'Median:{np.median(height)}')
# standard Deviation
print(f'Std:{np.std(height)}')
# 25th and 75th percentile
print(f'25th percentile:{np.percentile(height, 25)}')
print(f' 75th percentile:{np.percentile(height, 75)}')

#Number of president whose height is above average
print(f'The number of president whose height is above average is {np.sum(height>np.average(height))}')
#Number of president whose height is better than 75% data
print(f'The number of president whose height is better than 75% data is {np.sum(height>np.percentile(height,75))}')
#Number of president whose height is less than 25% data
print(f'The number of president whose height is less than 25% data is {np.sum(height<np.percentile(height,25))}')
#Find number of president whose height is maximum
print(f'The number of president whose height is max is {np.sum(height==np.max(height))}')

plt.hist(height)
plt.title("Height Distribution")
plt.xlabel("Height Range")
plt.ylabel("Height cm")
# plt.show()
plt.savefig("abc")

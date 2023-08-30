import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url,sep='\t')
print(chipo.head())
print(chipo.columns)

#Create a histogram of the top 5 items bought
item_name = chipo['item_name']
print(f'Item Name')
print(item_name)

#Using counter to create a dictionary
counts = Counter(item_name)
print(counts)

#Change it to datafraome ## passing orient to index to change key to rows
df = pd.DataFrame.from_dict(counts,orient='index')
print('Data Frame')
print(df)
print(df.columns)
print("Data Fromsss Sorted D-----------------ata")
sortedData = df[0].sort_values(ascending=False)
print(sortedData.head(6))
sortedDataFive = sortedData[:6]
print("Sorted Firve Itemssssssss")
print(sortedDataFive)

sortedDataFive.plot(kind='bar')
plt.xlabel('Items')
plt.ylabel('No ordered')
plt.title('TOP 5 ITEMS')
plt.show()

# Create a scatterplot with the number of items orderered per order price
chipo['item_price'] = [float(value[1:]) for value in chipo['item_price']]
print(chipo.head())

orders = chipo.groupby('order_id').sum()
print(orders)

plt.scatter(x=orders['item_price'],y=orders['quantity'],s=50,c='green')

plt.xlabel('Order Price')
plt.ylabel('Items ')
plt.title('Number of items ordered')
plt.show()


# myList = [1,2,3,4,5]
# newList=  [x * 2 for x in myList]
# print(newList)
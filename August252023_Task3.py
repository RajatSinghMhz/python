import numpy as np
import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
print('\n------Reading csv separated by \t-----------\n')
chipo = pd.read_csv(url,sep='\t')
print('\n------Printing first 10 record-----------\n')
print(chipo.head(10))
print('\n------Printing shape rows(data entry)-----------\n')
print (chipo.shape)
print(chipo.shape[0])
print('\n------Printing number of columns-----------\n')
print(chipo.shape[1])
print('\n------Column information of dataFrame-----------\n')
print(chipo.columns)
print('\n-----Index information of dataFrame-----------\n')
print(chipo.index)
print('\n------Most Ordered items using GroupBy----------\n')
'''
Here, most ordered items not only depends on frequency but also the quantity
Grouping is a must
'''
print(f'Sample data: {chipo.sample(2)}')
print('-------------------')
groupItem = chipo.groupby('item_name')
print(groupItem)
print('-------------------')
groupItem = chipo.groupby('item_name').sum()
print(groupItem)
print('-------------------')
groupItem= groupItem.sort_values(by='quantity',ascending=False)
print(groupItem)
print(groupItem.head(1))
print('-------------------')
groupItem = chipo.groupby('choice_description').sum()
groupItem= groupItem.sort_values(by='quantity',ascending=False)
print(groupItem.head(1))

totalItems = chipo['quantity'].sum()
print(totalItems)

print("-------")
print(chipo['item_price'].dtype)

print(chipo['item_price'].sample())

itemPriceFloatFn =  lambda  x  : float(x[1:])
chipo['item_price'] = chipo['item_price'].apply(itemPriceFloatFn)

print(chipo['item_price'].dtype)

totalRevenue = np.sum(chipo['quantity']*chipo['item_price'])
print(totalRevenue)
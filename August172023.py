import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#Boolean Masking COncept
rng=np.random.default_rng(seed=10001)
x=rng.integers(0,10,[3,5])
print(x)
print(x[x>5])

print('---------------------------')
dataFrame=pd.read_csv("Iris.csv")
SepalLengthCm=dataFrame["SepalLengthCm"]
SepalWidthCm=dataFrame["SepalWidthCm"]
PetalLengthCm=dataFrame["PetalLengthCm"]
PetalWidthCm=dataFrame["PetalWidthCm"]
print(SepalWidthCm)
print('------------------------------------------------------------------')
#Flower whose petal length is greater than 4 is large, less than 2 is small
petalLengthArray=np.array(PetalLengthCm)
petalWidthArray=np.array(PetalWidthCm)
sepalLengthArray=np.array(SepalLengthCm)
sepalWidthArray=np.array(SepalWidthCm)
print(f'Flowers with petal >4 as large is :{petalLengthArray[(petalLengthArray>4)]}')
print(f'Flowers with petal <2 as small is :{petalLengthArray[(petalLengthArray<=2)]}')
print(f'Flowers with petal as medium is :{petalLengthArray[((petalLengthArray>2) & (petalLengthArray<=4))]}')
print('------------------------------------------------------------------')
#Find total number of large, small and medium
print(f'Flowers with petal >4 as large is :{np.sum(petalLengthArray>4)}')
print(f'Flowers with petal <2 as small is :{np.sum(petalLengthArray<=2)}')
print(f'Flowers with petal medium is :{np.sum((petalLengthArray>2) & (petalLengthArray<=4))}')
#Which is most occured flower speicies and least occured.
#Average,max,min of sepal length,sepal width,petal length,petal width
print('----------------------------------------------------------')
print(f'Max of sepalLength is: {np.max(sepalLengthArray)}')
print(f'Min of sepalLength is: {np.min(sepalLengthArray)}')
print(f'Mean of sepalLength is: {np.mean(sepalLengthArray)}')
print(f'Median of sepalLength is: {np.median(sepalLengthArray)}')
print('----------------------------------------------------------')
print(f'Max of sepalWidth is: {np.max(sepalWidthArray)}')
print(f'Min of sepalWidth is: {np.min(sepalWidthArray)}')
print(f'Mean of sepalWidth is: {np.mean(sepalWidthArray)}')
print(f'Median of sepalWidth is: {np.median(sepalWidthArray)}')
print('----------------------------------------------------------')
print(f'Max of petalLength is: {np.max(petalLengthArray)}')
print(f'Min of petalLength is: {np.min(petalLengthArray)}')
print(f'Mean of petalLength is: {np.mean(petalLengthArray)}')
print(f'Median of petalLength is: {np.median(petalLengthArray)}')
print('----------------------------------------------------------')
print(f'Max of petalWidth is: {np.max(petalWidthArray)}')
print(f'Min of petalWidth is: {np.min(petalWidthArray)}')
print(f'Mean of petalWidth is: {np.mean(petalWidthArray)}')
print(f'Median of petalWidth is: {np.median(petalWidthArray)}')
print('----------------------------------------------------------')


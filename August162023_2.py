import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([11, 1, 3, 44])

print("For Greater")
print(x > y)
print("For Lesser")
print(x < y)
print("For Equal")
print(x == y)
print("For Not Equal")
print(x != y)
print('==================================')
print((x * x) > (x * 2))
print('==================================')
multiDimArray = np.arange(16).reshape(4, 4)
print(multiDimArray)
print(multiDimArray < 6)
print('----------------------------------')
rng=np.random.default_rng(seed=11001)
x=rng.integers(0,10,(3,5))
print(x)
print(f'For x<4:{np.sum(x>4)}')
print(f'For x<4:{np.sum(x<4)}')
print(f'For x>4 in column: {np.sum(x>4,axis=0)}')
print('===================================')
print("Check if any value is greater than 100")
print(np.any(x>100))
print("Check if all value is less than 100")
print(np.all(x<100))
print('------------------------')


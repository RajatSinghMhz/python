import pandas as pd
universityTown = []
file=open('university_towns.txt','r')
fileData = file.readlines()
for line in fileData:
    if '[edit]' in line:
        state = line
    else:
        universityTown.append((state,line))
print(universityTown)
print("=====")

townsdf = pd.DataFrame(universityTown,columns=['State','Region'])
print(townsdf)

def getCity(item):
    if '(' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

townsdf2 = townsdf.applymap(getCity)
print("=================")
print(townsdf2)
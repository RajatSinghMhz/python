import pandas as pd
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',sep='|', index_col='user_id')
print(users.head())
print(users.columns)

#Step 4. Discover what is the mean age per occupation
print("Grouped")
grouped = users.groupby('occupation')['age'].mean()
print(grouped)

#Discover the Male ratio per occupation and sort it from the most to the least
def changeToNumeric(x):
    if(x == 'M'):
        return  1
    if (x == 'F'):
        return 0

gender_in_number = users['gender'].apply(changeToNumeric)
users['gender'] = gender_in_number
print(users.head())

print("Group By Occupation and Calculate Sum of Gender")
groupedByGender = users.groupby('occupation')['gender'].sum()
print(groupedByGender.sort_values(ascending=False))
groupedByGenderRation = groupedByGender/users['occupation'].value_counts()*100
print(groupedByGenderRation.sort_values(ascending=False))

# Step 6. For each occupation, calculate the minimum and maximum ages
print(f"Mean {users.groupby('occupation')['age'].agg(['min','max'])}")

print(f"Mean {users.groupby(['occupation','gender'])['age'].mean()}")
import pandas as pd
df=pd.read_csv('titanic.csv')
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(df.iloc[888]['FamilySize'])

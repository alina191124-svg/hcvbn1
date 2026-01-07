import pandas as pd
df=pd.read_csv('titanic.csv')
print(len(df[(df['Sex']=='female')&(df['Pclass']==1)&(df['Survived'] == 1)]))
print(len(df[(df['Age']<18)&(df['Parch'] == 0)]))
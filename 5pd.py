import pandas as pd
df=pd.read_csv('titanic.csv')
print(f"Медианный возраст равен: {df['Age'].median()}")
df['Age'] = df['Age'].fillna(df['Age'].median())
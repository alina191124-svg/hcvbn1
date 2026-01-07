import pandas as pd
df=pd.read_csv('titanic.csv')
print("Кол-во сторк,столбцов,тип данных")
df.info()
print('Кол-во пассажиров: ', len(df))
print('Кол-во пропущенных значений в каждом столбце')
print(df.isnull().sum())

print(df['Age'].isnull().sum()) 
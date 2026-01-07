import pandas as pd
df=pd.read_csv('titanic.csv')
print(f"Средний возраст выживших: {df.groupby('Survived')['Age'].mean()[1]:.2f}")
print(f"Средний возраст погибших: {df.groupby('Survived')['Age'].mean()[0]:.2f}")
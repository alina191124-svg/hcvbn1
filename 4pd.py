import pandas as pd
df=pd.read_csv('titanic.csv')
print(f'{df[df['Pclass']==1]['Fare'].mean():.2f}')
print(f'{df[df['Pclass']==3]['Survived'].mean()*100:.2f}')
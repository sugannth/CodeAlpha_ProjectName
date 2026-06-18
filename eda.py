import pandas as pd
#read the csv
df = pd.read_csv(r"D:\25CS270\Intern\alpha1-exploratory data analysis\Titanic-Dataset.csv")

#display the dataset

print(df.head())
print(df.info())
print(df.describe())

#check for null values

print(df.isnull().sum())

#how many passengers survived
print(df['Survived'].value_counts())


#data visualisation
import seaborn as sns
import matplotlib.pyplot as plt
#survival chart

sns.countplot(x='Survived', data=df)

plt.title("Survival Count")
plt.show()
#passenger class chart
sns.countplot(x='Pclass', data=df)

plt.title("Passenger Class")
plt.show()

#age distribution chart
sns.histplot(df['Age'], bins=20)

plt.title("Age Distribution")
plt.show()

#save charts
plt.savefig("chart.png")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\25CS270\Intern\alpha3-data visualisation\netflix_titles.csv")

movies = len(df[df['type']=="Movie"])
shows = len(df[df['type']=="TV Show"])

print("="*50)
print("NETFLIX DATA VISUALIZATION REPORT")
print("="*50)
print(f"Total Movies   : {movies}")
print(f"Total TV Shows : {shows}")
print("="*50)

df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
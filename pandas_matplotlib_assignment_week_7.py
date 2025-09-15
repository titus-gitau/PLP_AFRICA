# Analyzing Data with Pandas and Visualizing Results with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


# Load and Explore the Dataset


iris_data = load_iris()
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())


# Task 2: Data Analysis


print("\nBasic statistics:")
print(df.describe())

print("\nAverage measurements per species:")
print(df.groupby('species').mean())

print("\nObservation: Setosa has the smallest petal size, Virginica the largest, Versicolor in between.")


# Task 3: Data Visualization


# 1. Line Chart
plt.figure(figsize=(8,5))
plt.plot(df['sepal length (cm)'][:30], marker='o', label='Sepal Length')
plt.title("Line Chart: Sepal Length (first 30 samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='petal length (cm)', data=df, ci=None, palette='Set2')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()



#  Scatter Plot
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='Set1')
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()



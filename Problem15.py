# 15. Use the dataset 'titanic'. The dataset contains 891 rows and contains
# information about the passengers who boarded the unfortunate Titanic
# ship. Use the Seaborn library to see if we can find any patterns in the data.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv('D:/College/TY Sem 5/DSML/DSML_PRACTICAL/Datasets/Titanic.csv')

# Display the first few rows of the dataset
print(titanic.head())

# Basic information
print(titanic.info())

# Summary statistics
print(titanic.describe(include='all'))

# Check for missing values
print(titanic.isnull().sum())

# Plot all types of graphs to find patterns in the data

# Survival Rate by Gender

sns.countplot(data=titanic, x='Sex', hue='Survived', palette='viridis')
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(['Did not survive', 'Survived'])
plt.show()

# Write a code to check how the price of the ticket (column
# name: 'fare') for each passenger is distributed by plotting a histogram.

sns.histplot(titanic['Fare'], bins=30, kde=True, color='red')
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()
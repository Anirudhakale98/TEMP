# 14. Use the covid_vaccine_statewise.csv dataset and perform the following
# analytics.
# A. Describe the dataset.
# B. Number of Males vaccinated
# C.. Number of females vaccinated

import pandas as pd

data = pd.read_csv('D:/College/TY Sem 5/DSML/DSML_PRACTICAL/Datasets/Covid Vaccine Statewise.csv')

print(data.describe())
print(data.info())

print(data['Male (Doses Administered)'].sum())
print(data['Female (Doses Administered)'].sum())

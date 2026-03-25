# 1) Import pandas and read in the banklist.csv file into a dataframe called banks.

import pandas as pd
banks=pd.read_csv("C:\\Users\\sanja\\OneDrive\\Desktop\\Banklist.csv")
print(banks)

# 2) Show the head of the dataframe.

 print(banks.head())

# 3) What are the column names?

print(banks.info())

# 4) How many States (ST) are represented in this data set?

 print(banks["ST"].nunique())

# 5) Get a list or array of all the states in the data set.

 print(banks["ST"].unique())

# 6) Top 5 states with most failed banks

 print(banks["ST"].value_counts().head(5))

# 7) Top 5 acquiring institutions

print(banks["Acquiring Institution"].value_counts().head(5))

# 8) State Bank of Texas acquisitions

print(((banks['Acquiring Institution'] == 'State Bank of Texas') & (banks['ST'] == 'TX')).sum())





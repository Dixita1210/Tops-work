# 1) Import pandas and read in the banklist.csv file into a dataframe called banks.

import pandas as pd
banks=pd.read_csv("C:\\Users\\sanja\\OneDrive\\Desktop\\DINKY_Tops\\Excel taks\\Banklist.csv")
# print(banks)

# 2) Show the head of the dataframe.

# print(banks.head())

# What are the column names?

# print(banks.info())

# print(banks.columns)

# How many States (ST) are represented in this data set?

# print(len(banks["ST"].unique()))
# print(banks["ST"].nunique())

# Get a list or array of all the states in the data set.

# print(banks["ST"].unique())

# Top 5 states with most failed banks

# print(banks["ST"].value_counts().head(5))


# Top 5 acquiring institutions

# print(banks["Acquiring Institution"].value_counts().head(5))

# State Bank of Texas acquisitions

# print(((banks['Acquiring Institution'] == 'State Bank of Texas') & (banks['ST'] == 'TX')).sum())






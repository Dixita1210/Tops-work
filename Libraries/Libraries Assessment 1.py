# 1) Import pandas and read in the banklist.csv file into a dataframe called banks.

import pandas as pd
banks=pd.read_csv("C:\\Users\\sanja\\OneDrive\\Desktop\\Banklist.csv")
print(banks)

# 2) Show the head of the dataframe.

 print(banks.head())

# 3) What are the column names?

print(banks.info())

# 4) How many States (ST) are represented in this data set?

 print(len(banks["ST"].unique()))

# 5) Get a list or array of all the states in the data set.

 print(banks["ST"].unique())





import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\sanja\\OneDrive\\Desktop\\DINKY_Tops\\Pandas\\Economics_data.csv")
# print(df)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# #1. Shape of dataset

# print(" Shape:", df.shape)

# # 2. Column names & data types

# print(" Data Types", df.dtypes)

#3. Unique stock indices

# print("Unique Stock indices-", df['Stock Index'].nunique())

#4. Date range

# print("Date Range-", df['Date'].min() , df['Date'].max())

#5. Missing values

# print( df.isnull().sum())

#6. Negative values check

# neg_values = (df.select_dtypes(include='number') < 0).sum()
# print(neg_values[neg_values > 0])

#7. GDP Growth summary

# print('GDP Growth Summary-',  df['GDP Growth (%)'].describe())

# 8. Zero or near-zero trading volume

# print("Zero or near Zero trading volume-", (df['Trading Volume'] <=0).sum())

# 9. Duplicate rows

# print(" Duplicate Rows:", df.duplicated().sum())

# 10. Outliers 

# GDP = df['GDP Growth (%)']

# Q1 = GDP.quantile(0.25)
# Q3 = GDP.quantile(0.75)

# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# outliers = GDP[(GDP < lower) | (GDP > upper)]

# print('GDP-',outliers)

# Gold = df['Gold Price (USD per Ounce)']

# Q1 = Gold.quantile(0.25)
# Q3 = Gold.quantile(0.75)

# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# outliers = Gold[(Gold < lower) | (Gold > upper)]

# print('Gold-',outliers)

# crudeoil = df['Crude Oil Price (USD per Barrel)']

# Q1 = crudeoil.quantile(0.25)
# Q3 = crudeoil.quantile(0.75)

# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# outliers = crudeoil[(crudeoil < lower) | (crudeoil > upper)]

# print('crudeoil-',outliers)


#11. Inflation Rate summary

# print(df['Inflation Rate (%)'].describe())

#12 Average unemployment rate

# print(df['Unemployment Rate (%)'].mean())

#13 index of highest number in trading volume 

# print(df['Trading Volume'].idamx)

#14 stock records from each index 

# print(df['Stock Index'].value_counts())

#15 What is the correlation between inflation and interest rate?

# print( df['Inflation Rate (%)'].corr(df['Interest Rate (%)']))

#16  Avg Consumer Confidence Index

# print( df['Consumer Confidence Index'].mean())

#17 Column with highest std deviation

# print(df.std(numeric_only=True).idxmax())

#18 Highest gold price 

# print(df['Gold Price (USD per Ounce)'].max())

#19 Date with highest crude oil price

# max_oil_idx = df['Crude Oil Price (USD per Barrel)'].idxmax()
# print( df.loc[max_oil_idx, 'Date'])

# 20. Average corporate profits

# print( df['Corporate Profits (Billion USD)'].mean())








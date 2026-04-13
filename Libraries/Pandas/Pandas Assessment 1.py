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

#Insight Analysis Questions 

# . What percentage of the dataset shows negative GDP growth?


neg_gdp = (df['GDP Growth'] < 0).sum()
total = len(df)
percentage = (neg_gdp / total) * 100
print( percentage)


# Does high inflation correspond to higher interest rates?

corr = df.corr(numeric_only=True)

print(corr)
#No because its 0.006 which is small

# Is there a relationship between unemployment and consumer spending?
print( corr['Unemployment Rate (%)']['Consumer Spending (Billion USD)'])
#NO relationship

# Do higher corporate profits align with higher consumer confidence?
print(corr['Corporate Profits']['Consumer Confidence'])
#no relationship

#What’s the trend of crude oil prices over time?
x = np.arange(len(df))

y = df['Crude Oil Price (USD per Barrel)']


plt.plot(x, y)


plt.title("Trend of Crude Oil Prices Over Time")
plt.xlabel("Time")
plt.ylabel("Crude Oil Price (USD per Barrel)")


plt.show()

#Are gold prices inversely related to stock performance?

print(corr['Gold Price (USD per Ounce)']['Close Price'])

#no 
# Does government debt impact consumer confidence?

print( corr['Government Debt (Billion USD)']['Consumer Confidence Index'])
#NO

#How do mergers & acquisitions (M&A) activity correlate with stock index closing prices?

print( corr['Mergers & Acquisitions Deals']['Close Price'])

#Is retail sales growth associated with GDP growth?

print( corr['Retail Sales (Billion USD)']['GDP Growth (%)'])
#NO

#Is stock market performance linked to consumer spending?

print( corr['Close Price']['Consumer Spending (Billion USD)'])
#NO

# Which stock index had the highest average closing price?

avg_close = df.groupby('Stock Index')['Close Price'].mean()
print( avg_close.idxmax())

 # What is the relationship between interest rate and unemployment?

print( corr['Interest Rate (%)']['Unemployment Rate (%)'])
#No relation

#Do lower consumer confidence values coincide with higher bankruptcy rates?

print( corr['Consumer Confidence Index']['Bankruptcy Rate (%)'])

#NO

#Which indicator has the highest correlation with stock close price?

print( corr['Close Price'].sort_values(ascending=False))

#Are unemployment rates lower when corporate profits are high?

print( corr['Unemployment Rate (%)']['Corporate Profits (Billion USD)'])

#NO
















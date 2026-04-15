import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#1. View the structure of the dataset (columns, types, missing values).
df=pd.read_csv("C:\\Users\\sanja\\OneDrive\\Desktop\\DINKY_Tops\\Pandas\\Retail Data.csv")
# print(df)
# print(df.info())

# 2. What is the shape (rows, columns) of the dataset?

# print(df.shape)

# 3. Are there any duplicate records?
#NO

# print(df.duplicated().sum())

# 4. Are there any missing or corrupted entries in Ship Date, Order Date, or numeric
# columns?

# print(df['Order Date'].isnull().sum())
# print(df['Ship Date'].isnull().sum())

# 5. Convert Order Date and Ship Date to datetime.

df['Order Date']=pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date']=pd.to_datetime(df['Ship Date'], errors='coerce')

# 6. Check for future or inconsistent shipping dates.

# invalid_shipping=df[df['Ship Date'] < df['Order Date']]
# print(len(invalid_shipping))


# 7. Convert price columns to numeric (remove $ and commas).

price_cols = ['Cost Price', 'Retail Price', 'Profit Margin',
              'Sub Total', 'Discount %', 'Discount $',
              'Order Total', 'Shipping Cost', 'Total']

for col in price_cols:
    df[col] = df[col].str.replace('$', '') 
    df[col] = df[col].str.replace(',', '') 
    df[col] = df[col].str.replace('%', '')   
    
    df[col] = pd.to_numeric(df[col])   

# 8. What are the unique values in Customer Type and Order Priority?

# print("\nCustomer Type:", df['Customer Type'].unique())
# print("Order Priority:", df['Order Priority'].unique())

# 9. What are the most common shipping modes?

# print( df['Ship Mode'].value_counts())


# 10. Which cities have the highest number of orders?

# print(df['City'].value_counts().head())

# 11. What’s the range of order quantities and prices?

# print("\nOrder Quantity Range:", df['Order Quantity'].min(), "-", df['Order Quantity'].max())

# for col in price_cols:
#     print(f"{col} Range:", df[col].min(), "-", df[col].max())


# 12. Create a new column for shipping duration.

# df['Shipping Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
# print("\nShipping Duration Created")

# 13. Are there any orders with zero or negative total or quantity?

# invalid_orders=df[(df["Order Quantity"]<=0) | (df['Total']<=0)]
# print(invalid_orders.shape[0])

# 14. Are all discount percentages matching discount dollar amounts?

# df['Expected Discount $'] = (df['Sub Total'] * df['Discount %']) / 100

# discount_mismatch = df[abs(df['Expected Discount $'] - df['Discount $']) > 1]
# print("\nDiscount Mismatches:", len(discount_mismatch))



# 15. Check for mismatches in total calculation

# df['Expected Total'] = df['Sub Total'] - df['Discount $'] + df['Shipping Cost']

# total_mismatch = df[abs(df['Expected Total'] - df['Total']) > 1]
# print("Total Mismatches:", len(total_mismatch))




# 16. Identify top 5 products by order quantity.

# top_products = df.groupby('Product Name')['Order Quantity'].sum().sort_values(ascending=False).head(5)
# print(top_products)



# 17. Which Account Manager handled the most revenue?

# manager_revenue = df.groupby('Account Manager')['Total'].sum().sort_values(ascending=False)
# print(manager_revenue.head(1))


# 18. What is the average shipping cost by mode?

# avg_shipping = df.groupby('Ship Mode')['Shipping Cost'].mean()
# print(avg_shipping)


# 19. Find the most profitable product.

# df['Profit']= df['Sub Total'] -(df['Cost Price'] * df['Order Quantity'])
# profit_product = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False)
# print( profit_product.head(1))



# 1. What is the total revenue generated across all orders?

# total_revenue = df['Total'].sum()
# print("Total Revenue:", total_revenue)

# 2. Which customer type generates more revenue?

# print(df.groupby('Customer Type')['Total'].sum().sort_values(ascending=False).head(1))

# 3. How does order priority affect revenue?

# print(df.groupby('Order Priority')['Total'].sum().sort_values(ascending=False))

# 4. What is the average profit margin by product category?

# print(df.groupby('Product Category')['Profit Margin'].mean())

# 5. What is the most profitable product overall?

df['Profit']= df['Sub Total'] -(df['Cost Price'] * df['Order Quantity'])
# print(df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(1))

# 6. How many days does it usually take to ship an order?

# df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
# print(df['Shipping Days'].mean())


# 7. Do longer shipping times impact profit margins?

# print(df[['Shipping Days', 'Profit Margin']].corr())
#Yes it reduced profit because corr is negative 

# 8. Which city brings in the highest revenue?

# print(df.groupby('City')['Total'].sum().sort_values(ascending=False).head(1))


# 9. Which account manager generated the most revenue?

# manager_revenue = df.groupby('Account Manager')['Total'].sum().sort_values(ascending=False)
# print(manager_revenue.head(1))



# 10. Which shipping mode is most cost-effective (lowest avg. shipping)?

# print(df.groupby('Ship Mode')['Shipping Cost'].mean().sort_values().head(1))

# 11. Do higher discounts reduce profits?

print(df[['Discount $', 'Profit']].corr())
#No because corr is positive


# 12. Which state has the highest number of orders?

print(df['State'].value_counts().head(1))

# 13. What is the average discount % across all orders?

print("Average Discount:", df['Discount $'].mean())


# 14. What is the average total spend per order?

print(df['Total'].mean())

# 15. . Are certain containers (e.g., Small Box, Wrap Bag) more profitable?

print(df.groupby('Product Container')['Profit'].mean().sort_values(ascending=False))

#small box is profitable more 


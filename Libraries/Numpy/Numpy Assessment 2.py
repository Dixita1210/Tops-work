import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("C:\\Users\\sanja\\OneDrive\\Desktop\\DINKY_Tops\\Numpy\\historical_automobile_sales.csv")

# print(df.head())
# print(df.info())
# print(df.describe())

#Q 1: Develop a Line chart using the functionality of pandas to show how automobile sales fluctuate from year to year.


# yearly_sales = df.groupby('Year')['Automobile_Sales'].sum()

# yearly_sales.plot(kind='line', marker='o')

# plt.title("Yearly Automobile Sales Trend")
# plt.xlabel("Year")
# plt.ylabel("Total Sales")
# plt.legend()
# plt.grid()
# plt.show()


#Q 2: Plot different lines for categories of vehicle type and analyze the trend
# to answer the question Is there a noticeable difference in sales trends
#between different vehicle types during recession periods? 

# vehicle_trend = df.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].sum().unstack()

# vehicle_trend.plot(marker='o')

# plt.title("Sales Trend by Vehicle Type")
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.legend(title="Vehicle Type")
# plt.grid()
# plt.show()


# Q 3: Use the functionality of Seaborn Library to create a visualization to compare
# the sales trend per vehicle type for a recession period with a non- recession
# period. 


# Q 4: Now you want to compare the sales of different vehicle types
# during a recession and a non-recession period 




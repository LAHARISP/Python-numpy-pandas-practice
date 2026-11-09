import pandas as pd
import numpy as np
# Read the CSV file using pd.read_csv().
df=pd.read_csv('dataset.csv')

# Task 2: Numerical Data Analysis
# 1. Extract the age column into a NumPy array.
print(df["age"])

# 2. Find the average customer age.
print("Avg customer age:",df["age"].mean())

# 3. Find the maximum and minimum customer age.
print("maximum customer age",df["age"].max())
print("minimum customer age",df["age"].min())

# 4. Calculate the median age.
print("median age:",df["age"].median())

# 5. Calculate the standard deviation of customer ages.
print("standard deviation age:",df["age"].std())

# 6. Find the average product price.
print("Average Product Price:", df["unit_price"].mean())

# 7. Find the total quantity of products sold.
print("Total Quantity Sold:", df["quantity"].sum())

# 8. Calculate the average discount percentage.
print("Average Discount:", df["discount_percent"].mean())

# 9. Find customers whose loyalty points are greater than 5,000.
customers = df[df["loyalty_points"] > 5000]
print(customers[["first_name","loyalty_points"]])

# 10. Create a NumPy array containing the first 20 customer ages.
ages = np.array(df["age"].head(20))
print(ages)

# # Task 3: NumPy Array Manipulation
# # 1. Create a NumPy array containing customer ages.
ages=np.array(df["age"])
print(ages)

# 2. Print the first 10 elements.
print(ages[:10])

# 3. Extract elements from index 10 to 20.
print(ages[10:21])

# 4. Reverse the array.
print(ages[::-1])

# 5. Sort the array in ascending order.
print(np.sort(ages))

# 6. Find unique customer ages.
print(np.unique(ages))

# 7. Count the number of unique ages.
print(len(np.unique(ages)))

# 8. Replace ages below 18 with 18 using np.where().
updated_ages = np.where(ages < 18, 18, ages)
print("\nUpdated Ages:")
print(updated_ages)

# 9. Calculate the square of every age.
print(np.square(ages))

# 10. Calculate the difference between the maximum and minimum age.
diff=np.max(ages)-np.min(ages)
print(diff)
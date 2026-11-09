# Import NumPy and Pandas.
import pandas as pd
import numpy as np
# Read the CSV file using pd.read_csv().
df=pd.read_csv('dataset.csv')
print(df.head())

# Display the first 5 records.
print(df[0:5])

# Display the last 10 records.
print(df[-10:])

# Display 10 random records.
print(df.sample(10))

# Find the total number of rows and columns.
print("Rows:",len(df))
print("Columns:",len(df.columns))

# Display all column names.
print(df.columns)

# Find the shape of the dataset.
print("shape of dataset",df.shape)

# Display the data types of all columns.
print(df.dtypes)

# Check the memory usage of the dataset.
print(df.memory_usage())

#print total no of elements
print(df.size)
import pandas as pd

# reading database in variables
data = pd.read_csv("/home/d/Documents/DSBDL/01/iris.csv")
new = pd.read_csv("/home/d/Documents/DSBDL/01/new.csv")

# printing whole databse
print(new)

# print first 5 rows in database
print(data.head())

# Check dimensions of dataframe
print(new.shape)

# Check whether null values are present in the database as per the column
print(new.isnull().sum())

# Get initial statistics for the data
print(new.describe())

# Convert a variable to integer
data['sepal.length'] = data['sepal.length'].astype(int)

# Check data types of variables in the dataframe
#print(data.dtypes)

# Perform categorical variable into quantitative variables
new_df = new.replace(to_replace=["Female","Male"],value=[0,1])
print(new_df)
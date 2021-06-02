# Imports
import pandas as pd
from sqlalchemy import create_engine

# This CSV doesn't have a header so pass
# column names as an argument
columns = [
  "sepal_length",
  "sepal_width",
  "petal_length",
  "petal_width",
  "class"
]

# Instantiate sqlachemy.create_engine object
engine = create_engine('postgresql://nikol:moonbeam@localhost:5432/books')

# Create an iterable that will read "chunksize=1000" rows
# at a time from the CSV file
for df in pd.read_csv("data/books.csv",names=columns,chunksize=1000):
  df.to_sql(
    'books',
    engine,
    index=False,
    if_exists='append' # if the table already exists, append this data
  )
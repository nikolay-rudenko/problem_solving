# Write data from CVS file to Postgress DB using Panda and SQLAlchemy

import pandas as pd
from sqlalchemy import create_engine

# This CSV doesn't have a header so pass
# column names as an argument
columns = [
  'book_title',
  'author',
  'publisher',
  'pub_date',
  'isbn'
]

# Instantiate sqlachemy.create_engine object
engine = create_engine('postgresql://nikol:moonbeam@localhost:5432/test')

# Create an iterable that will read "chunksize=1000" rows
# at a time from the CSV file
for df in pd.read_csv("data/books.csv", names=columns, chunksize=1000, header=None):
    df.to_sql(
        'books',
        engine,
        index=False,
        if_exists='append'  # if the table already exists, append this data
    )

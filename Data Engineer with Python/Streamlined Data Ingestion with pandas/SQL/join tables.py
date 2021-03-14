'''
Tables in relational databases usually have key columns of unique record identifiers. This lets us build pipelines that combine tables using SQL's JOIN operation, instead of having to combine data after importing it.

The records in hpd311calls often concern issues, like leaks or heating problems, that are exacerbated by weather conditions. In this exercise, you'll join weather data to call records along their common date columns to get everything in one data frame. You can assume these columns have the same data type.

pandas is loaded as pd, and the database engine, engine, has been created.

Note: The SQL checker is picky about join table order -- it expects specific tables on the left and the right.

Instructions
100 XP
Complete the query to join weather to hpd311calls by their date and created_date columns, respectively.
Query the database and assign the resulting data frame to calls_with_weather.
Print the first few rows of calls_with_weather to confirm all columns were joined.
'''

# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Create the database engine
engine = create_engine("sqlite:///c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/data.db")


# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create data frame of joined tables
calls_with_weather = pd.read_sql(query,engine)

# View the data frame to make sure all columns were joined
print(calls_with_weather.head())

# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query,engine)

# View the data frame
print(leak_calls.head())

# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
  WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())

# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())

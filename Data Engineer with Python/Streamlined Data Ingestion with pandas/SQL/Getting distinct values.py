'''
Sometimes an analysis doesn't need every record, but rather unique values in one or more columns. Duplicate values can be removed after loading data into a data frame, but it can also be done at import with SQL's DISTINCT keyword.

Since hpd311calls contains data about housing issues, we would expect most records to have a borough listed. Let's test this assumption by querying unique complaint_type/borough combinations.

pandas has been imported as pd, and the database engine has been created as engine.

Note: The SQL checker is quite picky about column positions and expects fields to be selected in the specified order.

Instructions
100 XP
Create a query that gets DISTINCT values for borough and complaint_type (in that order) from hpd311calls.
Use read_sql() to load the results of the query to a data frame, issues_and_boros.
Print the data frame to check if the assumption that all issues besides literature requests appear with boroughs listed.
'''

# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Create the database engine
engine = create_engine("sqlite:///c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/data.db")


# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  from hpd311calls;
"""

# Load results of query to a data frame
issues_and_boros = pd.read_sql(query,engine)

# Check assumption about issues and boroughs
print(issues_and_boros)


# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
     COUNT(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# Create data frame of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()

# Create a query to get month and max tmax by month
query = """
SELECT month, 
       MAX(tmax)
  FROM weather 
  GROUP BY month;"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

# Create a query to get month, max tmax, and min tmin by month
query = """
SELECT month, 
	   MAX(tmax), 
       MIN(tmin)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

# Create query to get temperature and precipitation by month
query = """
SELECT month, 
       MAX(tmax), 
       MIN(tmin),
       SUM(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)
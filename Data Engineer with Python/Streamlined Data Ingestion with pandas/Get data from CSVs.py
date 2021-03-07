'''
Get data from CSVs
In this exercise, you'll create a data frame from a CSV file. The United States makes available CSV files containing tax data by ZIP or postal code, allowing us to analyze income information in different parts of the country. We'll focus on a subset of the data, vt_tax_data_2016.csv, which has select tax statistics by ZIP code in Vermont in 2016.

To load the data, you'll need to import the pandas library, then read vt_tax_data_2016.csv and assign the resulting data frame to a variable. Then we'll have a look at the data.

Import the pandas library as pd.
Use read_csv() to load vt_tax_data_2016.csv and assign it to the variable data.
View the first few lines of the data frame with the head() method. This code has been written for you.

'''

# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv('vt_tax_data_2016.tsv', sep='\t')

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()
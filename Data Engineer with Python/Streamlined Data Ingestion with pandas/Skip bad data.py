'''
In this exercise you'll use read_csv() parameters to handle files with bad data, like records with more values than columns. By default, trying to import such files triggers a specific error, pandas.io.common.CParserError.

Some lines in the Vermont tax data here are corrupted. In order to load the good lines, we need to tell pandas to skip errors. We also want pandas to warn us when it skips a line so we know the scope of data issues.

pandas has been imported as pd. The exercise code will try to read the file. If there is a pandas.io.common.CParserError, the code in the except block will run.

Instructions 1/3
35 XP
Try to import the file vt_tax_data_2016_corrupt.csv without any keyword arguments.

Import vt_tax_data_2016_corrupt.csv with the error_bad_lines parameter set to skip bad records.

Update the import with the warn_bad_lines parameter set to issue a warning whenever a bad record is skipped.
'''

import pandas as pd

names = []

# Create data frame of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/vt_tax_data_2016.csv",
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=names)

try:
    # Import the CSV without any keyword arguments
    data = pd.read_csv("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/vt_tax_data_2016.csv")

    # View first 5 records
    print(data.head())

except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")

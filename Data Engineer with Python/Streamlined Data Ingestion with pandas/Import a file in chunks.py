'''
Import a file in chunks
When working with large files, it can be easier to load and process the data in pieces. Let's practice this workflow on the Vermont tax data.

The first 500 rows have been loaded as vt_data_first500. You'll get the next 500 rows. To do this, you'll employ several keyword arguments: nrows and skiprows to get the correct records, header to tell pandas the data does not have column names, and names to supply the missing column names. You'll also want to use the list() function to get column names from vt_data_first500 to reuse.

pandas has been imported as pd.

Instructions
0 XP
Use nrows and skiprows to make a data frame, vt_data_next500, with the next 500 rows.
Set the header argument so that pandas knows there is no header row.
Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.

Hint
Because we already read the first 500 rows and are trying to get the next 500, nrows and skiprows should take the same integer.
The keyword None tells pandas that there is no header in the data.
You can get a list of a data frame's column names by passing the data frame to list().
'''

import pandas as pd

names = ['STATEFIPS',
 'STATE',
 'zipcode',
 'agi_stub',
 'N1',
 'mars1',
 'MARS2',
 'MARS4',
 'PREP',
 'N2',
 'NUMDEP',
 'TOTAL_VITA',
 'VITA',
 'TCE',
 'VITA_EIC',
 'RAL',
 'RAC',
 'ELDERLY',
 'A00100',
 'N02650',
 'A02650',
 'N00200',
 'A00200',
 'N00300',
 'A00300',
 'N00600',
 'A00600',
 'N00650',
 'A00650',
 'N00700',
 'A00700',
 'N00900',
 'A00900',
 'N01000',
 'A01000',
 'N01400',
 'A01400',
 'N01700',
 'A01700',
 'SCHF',
 'N02300',
 'A02300',
 'N02500',
 'A02500',
 'N26270',
 'A26270',
 'N02900',
 'A02900',
 'N03220',
 'A03220',
 'N03300',
 'A03300',
 'N03270',
 'A03270',
 'N03150',
 'A03150',
 'N03210',
 'A03210',
 'N03230',
 'A03230',
 'N03240',
 'A03240',
 'N04470',
 'A04470',
 'A00101',
 'N17000',
 'A17000',
 'N18425',
 'A18425',
 'N18450',
 'A18450',
 'N18500',
 'A18500',
 'N18800',
 'A18800',
 'N18300',
 'A18300',
 'N19300',
 'A19300',
 'N19500',
 'A19500',
 'N19530',
 'A19530',
 'N19550',
 'A19550',
 'N19570',
 'A19570',
 'N19700',
 'A19700',
 'N20800',
 'A20800',
 'n21020',
 'a21020',
 'N04800',
 'A04800',
 'N05800',
 'A05800',
 'N09600',
 'A09600',
 'N05780',
 'A05780',
 'N07100',
 'A07100',
 'N07300',
 'A07300',
 'N07180',
 'A07180',
 'N07230',
 'A07230',
 'N07240',
 'A07240',
 'N07220',
 'A07220',
 'N07260',
 'A07260',
 'N09400',
 'A09400',
 'N85770',
 'A85770',
 'N85775',
 'A85775',
 'N09750',
 'A09750',
 'N10600',
 'A10600',
 'N59660',
 'A59660',
 'N59720',
 'A59720',
 'N11070',
 'A11070',
 'N10960',
 'A10960',
 'N11560',
 'A11560',
 'N06500',
 'A06500',
 'N10300',
 'A10300',
 'N85530',
 'A85530',
 'N85300',
 'A85300',
 'N11901',
 'A11901',
 'N11902',
 'A11902']

# Create data frame of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/vt_tax_data_2016.csv",
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=names)

# View the Vermont data frames to confirm they're different
#print(vt_data_first500.head())
print(vt_data_next500.head())

print(vt_data_next500.dtypes)

# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode":0}

# Load csv using na_values keyword argument
data = pd.read_csv("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/vt_tax_data_2016.csv",
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])
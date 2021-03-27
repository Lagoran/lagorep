'''
Iterating with .itertuples()
Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple. You can look up an attribute within a namedtuple with a special syntax. Let's practice working with namedtuples.

A pandas DataFrame has been loaded into your session called rangers_df. This DataFrame contains the stats ('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs') for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').

Instructions 1/3
35 XP
Use .itertuples() to loop over rangers_df and print each row.

Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.

Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs.
'''

import pandas as pd
import matplotlib.pyplot as plt

rangers_df=pd.DataFrame({'Team':[
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX',
'TEX'],
                         'League':['AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
'AL',
],
                         'Year':['2012',
'2011',
'2010',
'2009',
'2008',
'2007',
'2006',
'2005',
'2004',
'2003',
'2002',
'2001',
'2000',
'1999',
'1998',
'1997',
'1996',
'1993',
'1992',
'1991',
'1990',
'1989',
'1988',
'1987',
'1986',
'1985',
'1984',
'1983',
'1982',
'1980',
'1979',
'1978',
'1977',
'1976',
'1975',
'1974',
'1973',
],
                         'RS':['808',
'855',
'787',
'784',
'901',
'816',
'835',
'865',
'860',
'826',
'843',
'890',
'848',
'945',
'940',
'807',
'928',
'835',
'682',
'829',
'676',
'695',
'637',
'823',
'771',
'617',
'656',
'639',
'590',
'756',
'750',
'692',
'767',
'616',
'714',
'690',
'619',
],
                         'RA':['707',
'677',
'687',
'740',
'967',
'844',
'784',
'858',
'794',
'969',
'882',
'968',
'974',
'859',
'871',
'823',
'799',
'751',
'753',
'814',
'696',
'714',
'735',
'849',
'743',
'785',
'714',
'609',
'749',
'752',
'698',
'632',
'657',
'652',
'733',
'698',
'844',
],
                         'W':['93',
'96',
'90',
'87',
'79',
'75',
'80',
'79',
'89',
'71',
'72',
'73',
'71',
'95',
'88',
'77',
'90',
'86',
'77',
'85',
'83',
'83',
'70',
'75',
'87',
'62',
'69',
'77',
'64',
'76',
'83',
'87',
'94',
'76',
'79',
'83',
'57',
],
                         'G':['162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'162',
'163',
'162',
'162',
'162',
'162',
'162',
'161',
'162',
'162',
'161',
'161',
'163',
'162',
'163',
'162',
'162',
'162',
'162',
'162',
'161',
'162',
],
                         'Playoffs':['1',
'1',
'1',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'1',
'1',
'0',
'1',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0'
]
                         })

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

    # reference
    #
    # df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
    #                               'Parrot', 'Parrot'],
    #                    'Max Speed': [380., 370., 24., 26.]})
# print(rangers_df.head())

def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'


# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)
  print(type(row))

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
      print(i, year, wins)

# # Loop over the DataFrame and print each row's Index, Year and Wins (W)
# for row in rangers_df.itertuples():
#     i = row.Index
#     year = row.Year
#     wins = row.W

    #run_diffs=[]

    # Loop over the DataFrame and calculate each row's run differential
    # for row in rangers_df.itertuples():
    #     runs_scored = int(row.RS)
    #     runs_allowed = int(row.RA)
    #
    #     run_diff = calc_run_diff(runs_scored, runs_allowed)
    #
    #     run_diffs.append(run_diff)

# Append new column
# rangers_df['RD'] = run_diffs
# print(rangers_df)

#the idea here is to replace the looping over dataframe rows and replace this action with the .apply attribute of the df
#which should be much more efficient
run_diff_apply=rangers_df.apply(
    lambda row: calc_run_diff(int(row['RS']),int(row['RA'])),
    axis=1
)

rangers_df['RD']=run_diff_apply

print(rangers_df.head())

plt.plot(rangers_df['Year'], rangers_df['RD'])
# plt.plot(rangers_df['Year'], rangers_df['Playoffs'])
plt.show()

print(type(rangers_df['Year']))


# create an dataframe from the existing one omitting non-int columns
#new = old[['A', 'C', 'D']].copy()
#https://stackoverflow.com/questions/34682828/extracting-specific-selected-columns-to-new-dataframe-as-a-copy

#
# rangers_int_df = rangers_df[['RS', 'RA', 'W', 'G', 'Playoffs', 'RD']]
# print(rangers_int_df.head())
# rangers_int_df.describe()
# rangers_int_df.info()

#>>> pd.to_numeric(s) # convert everything to float values
# convert all columns of DataFrame
#df = df.apply(pd.to_numeric) # convert all columns of DataFrame

rangers_int_df = rangers_df[['RS', 'RA', 'W', 'G', 'Playoffs', 'RD']].apply(pd.to_numeric)
print(rangers_int_df.head())
rangers_int_df.describe()
rangers_int_df.info()

# Gather sum of all columns by per column level
stat_totals = rangers_int_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rangers_int_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored.head())

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rangers_int_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs.head())
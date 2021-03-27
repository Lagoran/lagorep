'''
Settle a debate with .apply()
Word has gotten to the Arizona Diamondbacks about your awesome analytics skills. They'd like for you to help settle a debate amongst the managers. One manager claims that the team has made the playoffs every year they have had a win percentage of 0.50 or greater. Another manager says this is not true.

Let's use the below function and the .apply() method to see which manager is correct.

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)
A DataFrame named dbacks_df has been loaded into your session.

Instructions 1/4
1 XP
Print the first five rows of the dbacks_df DataFrame to see what the data looks like.

Hint
Use the .head() method to display the first few rows of a DataFrame.
'''

import numpy as np
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



def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)


# Display the first five rows of the DataFrame
# print(rangers_df.head())
# rangers_df.describe()

rangers_int_df = rangers_df[['RS', 'RA', 'W', 'G', 'Playoffs']].apply(pd.to_numeric)
print(rangers_int_df.head())
rangers_int_df.describe()
rangers_int_df.info()

# Create a win percentage Series
win_percs = rangers_int_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

plt.plot(win_percs)
# plt.plot(rangers_df['Year'], rangers_df['Playoffs'])
plt.show()

# Append a new column to rangers_int_df
rangers_int_df['WP'] = win_percs
print(rangers_int_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(rangers_int_df[rangers_int_df['WP'] >= 0.50])
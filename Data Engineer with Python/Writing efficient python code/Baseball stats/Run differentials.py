'''
Run differentials with .iterrows()
You've been hired by the San Francisco Giants as an analyst—congrats! The team's owner wants you to calculate a metric called the run differential for each season from the year 2008 to 2012. This metric is calculated by subtracting the total number of runs a team allowed in a season from the team's total number of runs scored in a season. 'RS' means runs scored and 'RA' means runs allowed.

The below function calculates this metric:

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff
A DataFrame has been loaded into your session as giants_df and printed into the console. Let's practice using .iterrows() to add a run differential column to this DataFrame.

Instructions 4/4
0 XP
Add a line to the loop that appends each row's run differential to the run_diffs list.

'''

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

import pandas as pd

basket_df=pd.read_csv('c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/baseball_stats.csv')

# print(basket_df.head())

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i, row in basket_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)

    # Append each run differential to the output list
    run_diffs.append(run_diff)

basket_df['RD'] = run_diffs
# print(basket_df)

fileter1=basket_df.groupby(['Team'])
print(fileter1.head())



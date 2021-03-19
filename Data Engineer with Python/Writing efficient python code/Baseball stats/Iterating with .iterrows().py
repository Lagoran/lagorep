'''
Iterating with .iterrows()
In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs. But, what does this mean? Let's explore with a few coding exercises.

A pandas DataFrame has been loaded into your session called pit_df. This DataFrame contains the stats for the Major League Baseball team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012. It has been printed into your console for convenience.

Instructions 1/4
30 XP
Use .iterrows() to loop over pit_df and print each row. Save the first item from .iterrows() as i and the second as row.

Add two lines to the loop: one before print(row) to print each index variable and one after to print each row's type.

Instead of using i and row in the for statement to store the output of .iterrows(), use one variable named row_tuple.

Add a line in the for loop to print the type of each row_tuple.


***

Nice work! Since .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs, you can either split this tuple and use the index and row-values separately (as you did with for i,row in pit_df.iterrows()), or you can keep the result of .iterrows() in the tuple form (as you did with for row_tuple in pit_df.iterrows()).

If using i,row, you can access things from the row using square brackets (i.e., row['Team']). If using row_tuple, you would have to specify which element of the tuple you'd like to access before grabbing the team name (i.e., row_tuple[1]['Team']).

With either approach, using .iterrows() will still be substantially faster than using .iloc as you saw in the video.
'''

import pandas as pd

basket_df=pd.read_csv('c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/baseball_stats.csv')

print(basket_df.head())

# Iterate over pit_df and print each row
#for i,row in basket_df.iterrows():
#    print(row)

# Iterate over pit_df and print each index variable and then each row
#  for i,row in basket_df.iterrows():
#    print(i)
#    print(row)
#    print(type(row))

# Use one variable instead of two to store the result of .iterrows()
# for row_tuple in basket_df.iterrows():
#     print(row_tuple)

# Print the row and type of each row
for row_tuple in basket_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))




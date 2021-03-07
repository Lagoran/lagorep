'''
CSV to DataFrame (2)
Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what we wanted. The row labels were imported as another column without a name.

Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used as a row label? Well, that's exactly what you need here!

Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?

Instructions
100 XP
Run the code with Run Code and assert that the first column should actually be used as row labels.
Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
Has the printout of cars improved now?

Take Hint (-30 XP)

'''

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
#cars = pd.read_csv('c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/CARS.csv')

cars = pd.read_csv('c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/CARS.csv', index_col=0)

# Print out cars
print(cars)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

# Print out first 3 observations
print (cars[0:3])

# Print out fourth, fifth and sixth observation
print (cars[3:6])

# Print out observation for Japan
print(cars.loc['JAP'])

print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])
print(cars.iloc[[5], [2]])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])
print(cars.iloc[[4,5],[1,2]])

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])
print(cars.iloc[:,2])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])
print(cars.iloc[:,[2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['drives_right','cars_per_cap']])
print(cars.iloc[:,[0,2]])
'''
Driving right (1)
Remember that cars dataset, containing the cars per 1000 people (cars_per_cap) and whether people drive right (drives_right) for different countries (country)? The code that imports this data in CSV format into Python as a DataFrame is available on the right.

In the video, you saw a step-by-step approach to filter observations from a DataFrame based on boolean arrays. Let's start simple and try to find all observations in cars where drives_right is True.

drives_right is a boolean column, so you'll have to extract it as a Series and then use this boolean Series to select observations from cars.

Instructions
100 XP
Extract the drives_right column as a Pandas Series and store it as dr.
Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
Print sel, and assert that drives_right is True for all observations.

Take Hint (-30 XP)
'''

# Import pandas as pd
import pandas as pd

# Import numpy as np
import numpy as np

# Fix import by including index_col
#cars = pd.read_csv('c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/CARS.csv')

cars = pd.read_csv('c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/CARS.csv', index_col=0)


# Extract drives_right column as Series: dr
#dr = cars.iloc[:, 2]

# Use dr to subset cars: sel
#sel = cars[dr]
sel = cars[cars.iloc[:, 2]]

# Print sel
print(sel)


# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]


# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)
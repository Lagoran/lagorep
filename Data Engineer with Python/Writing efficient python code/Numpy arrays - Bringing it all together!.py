'''
Bringing it all together: Festivus!
In this exercise, you will be throwing a party—a Festivus if you will!

You have a list of guests (the names list). Each guest, for whatever reason, has decided to show up to the party in 10-minute increments. For example, Jerry shows up to Festivus 10 minutes into the party's start time, Kramer shows up 20 minutes into the party, and so on and so forth.

We want to write a few simple lines of code, using the built-ins we have covered, to welcome each of your guests and let them know how many minutes late they are to your party. Note that numpy has been imported into your session as np and the names list has been loaded as well.

Let's welcome your guests!

Instructions 1/4
25 XP
Use range() to create a list of arrival times (10 through 50 incremented by 10). Create the list arrival_times by unpacking the range object.

'''
# Create a list of arrival times
arrival_times = [*range(10, 51, 10)]

print(arrival_times)

import numpy as np

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']


# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)

# Create a list of arrival times
arrival_times = [*range(10,60,10)]


# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

print(guest_arrivals)
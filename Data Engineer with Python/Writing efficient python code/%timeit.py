'''
Using %timeit: your turn!
You'd like to create a list of integers from 0 to 50 using the range() function. However, you are unsure whether using list comprehension or unpacking the range object into a list is faster. Let's use %timeit to find the best implementation.

For your convenience, a reference table of time orders of magnitude is provided below (faster at the top).

symbol	name	unit (s)
ns	nanosecond	10-9
µs (us)	microsecond	10-6
ms	millisecond	10-3
s	second	100
Instructions 1/3
35 XP
Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.

'''
import time

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)

#enu_time = %timeit -o nums_list_comp = [num for num in range(51)]
#unpack_time = %timeit -o nums_unpack = [*range(51)]

%timeit nums_list_comp = [num for num in range(51)]
%timeit nums_unpack = [*range(51)]

diff = (enu_time.average - unpack_time.average)*(10**9)
print('Unpack time is better that cycle time by {} ns'.format(diff))

#In [1]:
#%timeit nums_list_comp = [num for num in range(51)]
#2.26 us +- 121 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
#In [2]:
#%timeit nums_unpack = [*range(51)]
#469 ns +- 64.3 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
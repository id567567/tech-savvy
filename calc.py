# Exercise 2.1

NUMBER_OF_SECONDS_IN_ONE_MINUTE = 60

seconds = 42 * NUMBER_OF_SECONDS_IN_ONE_MINUTE + 42

print("There are {} seconds...".format(seconds))

# Exercise 2.2

NUMBER_OF_KILOMETERS_IN_A_MILE = 1.61

miles = 10/NUMBER_OF_KILOMETERS_IN_A_MILE

print("There are {:.2f} miles in 10 kilometers.".format(miles))

print('my name is {:.3}.'.format("Maddison"))


# Exercise 1.1 in Chapter 1

import math
r = input("Please enter a number:")
print(type(r))

r = float(r)
print('After conversion,', type(r))

volume = (4/3)*math.pi*math.pow(r, 3)
print('The volume is of a sphere of {} is {:.3f].'.format(r, volume))


#1.3

hour = 13
min = 2

print("current time is {:02}:{:02}.".format(hour, min))

print(1+2)

import datetime
print(datetime.datetime.now())



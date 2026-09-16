import math

import var

# Excercise: Lvl 1
print("Day 2:30 Days of python programming")

firstname = input()
lastname = input()
fullname = firstname + " " + lastname
country = input()
city = input()
age = input()
is_married, is_true, is_light_on =  False, True, True


#Excersize: Lvl 2
print(type(firstname))
print(len(firstname))

"""
User Walrus Operator to create the variable and print it at the exact same time
"""
print(difference := len(firstname) - len(lastname))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = input()
area_of_circle = math.pi * radius ** 2
circum_of_circle = radius * 2 * math.pi


# Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.

# The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given.

# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.

# The program should display the following details:

# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over


#HOT DOG COOKOUT CALCULATOR

import math

# Get input from user
num_people = int(input("Enter the number of people attending the cookout: "))
num_hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Calculate the total number of hot dogs needed
total_hotdogs = num_people * num_hotdogs_per_person

# Calculate the minimum number of hot dog packages needed
hotdog_packages = math.ceil(total_hotdogs / 10)

# Calculate the minimum number of hot dog bun packages needed
bun_packages = math.ceil(total_hotdogs / 8)

# Calculate the number of hot dogs and buns left over
hotdogs_leftover = (hotdog_packages * 10) - total_hotdogs
buns_leftover = (bun_packages * 8) - total_hotdogs

# Output the results
print("\nMinimum number of hot dog packages required: ", hotdog_packages)
print("Minimum number of hot dog bun packages required: ", bun_packages)
print("Number of hot dogs left over: ", hotdogs_leftover)
print("Number of hot dog buns left over: ", buns_leftover)
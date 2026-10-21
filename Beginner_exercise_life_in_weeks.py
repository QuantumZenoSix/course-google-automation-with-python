#!/usr/bin/python

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age) # assume we live to be 90
months_left = int(years_left * 12)
weeks_left =int(years_left * 52)
days_left = int(years_left * 365) 

message = f"You have {months_left} months, {weeks_left} weeks, and {days_left} days left"
print (message)

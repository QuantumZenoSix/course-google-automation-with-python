#!/usr/bin/python3

# Basic List Comprehension
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]


answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]


# Making a quick nested loop
answer = [[i for i in range(0,3)] for num in range(0,3)] 


# Make this using list comprehension
    # [
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #  ]
answer = [[i for i in range(0,10)] for num in range(0,10)] 


# Dictionary comprehenstion to create state abbreviations
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0,3)}

# Using zip
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
dict(zip(list1,list2))  


# Dicitonary to list [Method 1]
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}


# Dicitonary to list [Method 2]
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}


# Dicitonary to list [Method 3 - BEST]
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)


# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)


# Get val with greatest magnitude
max_magnitude = lambda ls: max( abs(n) for n in ls )


# define sum_even_values
sum_even_values = lambda *args: sum([ n for n in args if n % 2 == 0 ])


# define sum_float_values
def sum_floats(*args):
    return sum( n for n in args if type(n) is float )


# Interleaving Strings
def interleave(s1, s2):
    return ''.join([tup[0] + tup[1] for tup in list(zip(s1,s2))])


#'Write a function called triple_and_filter. This function should accept a list of numbers, filter out every number that is not divisible by 4, and return a new list where every remaining number is tripled.'
def triple_and_filter(nums):
    return [x * 3 for x in filter(lambda n: n % 4 == 0 ,nums)]


# 'Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.'
def extract_full_name(dicts):
    return ['{} {}'.format(user['first'],user['last']) for user in dicts]
    # Using Map -> return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

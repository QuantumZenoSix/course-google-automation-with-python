#!/usr/bin/python


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator\n")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percent would you like to give? 10, 12, or 15? ")) / 100
num_of_people = int(input("How many people are splitting the bill? "))

tip_value = tip_percentage * bill
grand_total = bill + tip_value 
# bll_per_person = round(grand_total / num_of_people, 2) 
# (^ above) REMOVED -> learned 'format' function would be better here. Round doesn't guarantee two decimal places if ends in zero (i.e. 1.60 becomes 1.6)
bll_per_person = "{:.2f}".format(grand_total / num_of_people, 2) 

message = f"Each person should pay ${bll_per_person}"
print(message)

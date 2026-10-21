#!/usr/bin/python

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(int(weight) / (float(height) ** 2))
bmi_diagnosis = "clinically obsese" if bmi > 35 else "obese" if bmi > 30 else "overweight" if  bmi > 25 else "of normal weight" if bmi > 18.5 else "underweight"
print(f"{bmi} - you are {bmi_diagnosis}")

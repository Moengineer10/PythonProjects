# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:24:20 2023

@author: moham
"""

## Enter height
height = float(input("Enter your height: "))

## Enter weight
weight = int(input("Enter your weight: "))

## BMI Calc
bmi = weight / (height * height)

if bmi > 35:
    print("Your BMI is " + str(bmi) + ", you are clinically obese.")
elif 30 < bmi <=35:
    print("Your BMI is " + str(bmi) + ", you are obese.")
elif 25 < bmi <=30:
    print("Your BMI is " + str(bmi) + ", you are slighty overweight.")
elif 18.5 < bmi < 25: 
    print("Your BMI is " + str(bmi) + ", you are normal.")
else: 
    print("Your BMI is " + str(bmi) + ", you are underweight.")
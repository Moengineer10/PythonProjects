# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:19:23 2023

@author: moham
"""

print('Welcome to the tip calculator.')

a= input("What was the total bill?")
print('$', a)

b=  input("How many people to split the bill?")

print(b)


c=  input("What percentage tip would you like to give?")

print('%',c)

d= ((float(a)*float(c))/100)/int(b)+ (float(a)/int(b))

print('Each person should pay:', '$', round(d,3))
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:43:34 2023

@author: moham
"""
## VERSION 1
### Pizza Order Practice

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # what size pizza do you want? S, M or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

## Dont change the code above 

## Write your code below this line

## Initial pizza price
price = 0

if size == "S":
    price += 15
    #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
elif size == "M":
    price += 20
    #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
    
else:
    price += 25
    #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
    
    
    
if add_pepperoni == "Y" and size == "S":
        price += 2
        #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
elif add_pepperoni == "Y" and size == "M":
        price += 3
        #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
elif add_pepperoni == "Y" and size == "L":
        price += 3
        #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
else:
    price = price
    #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
    
    
        
if extra_cheese == "Y":
    price += 1
    print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")







    
#### VERSION 2

### Pizza Order Practice

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # what size pizza do you want? S, M or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

## Dont change the code above 

## Write your code below this line

## Initial pizza price
price = 0

if size == "S":
    price += 15
    #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
elif size == "M":
    price += 20
    #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
    
else:
    price += 25
    #print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
    
    
    
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price +=3

        
if extra_cheese == "Y":
    price += 1
print(f"Thank you for choosing Python Pizza Deliveries. Your final bill is ${price}")
    
    
    
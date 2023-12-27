# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 08:44:38 2023

@author: moham
"""

print('''
      
 __
                /__`.
               / \\ `\\
              /   \\  `\\
             /     \\   \\
            /_______\\  /\\
            (((( ))))
           (((' . ')))
           (((\\_-_/)))
           (((_) (_)))
          /((( \\ / )))\\
         / (((  ^  ))) \\
        / / ((  ^  )) \\ \\
       ( (   \\  ^  /   ) )
        \\ \\   )www(   / /
         `\\\\ /     \\ //'
           /'       `\\
          /           \\
         /             \\
        /               \\
       /                 \\
      /                   \\
     /                     \\
    /                       \\
   /                         \\
  /                           \\ jgs
 |                             |
  `-----......_____......-----'      
      
      
''')





print("Welcome to *** Save The Princess*** ")

print("Your mission is to save the heiress to the throne from the insurgents. She was kidnapped and is being held in one of the secret chambers of the castle.")

choice1 = input("You \'re at cross road and have to make a choice between searching the courtyard or the dungeon. Type 'left' to search the courtyard or 'right' to reach the dungeon: ").lower()

if choice1 == "left":
    choice2 = input("You have successfully entered the dungeon and have to choose between a metallic door and wooden door. Type 'metallic' or 'wooden': ").lower()
    
elif  choice1 == "right":
    print("You've been outnumbered by insurgents. GAME OVER!!!")
    
else:
    print("Wrong command!!!")
    
if choice2 == "metallic":
     choice3 = input("You have found the room where the princess is held but the door is locked. Type '1' to use a bobby pin, '2' to force your way in,'3' to call a locksmith: ").lower()
     
elif choice2 == "wooden":
    print("You \'ve opened the wrong door leading to the kennel. The dogs have alerted the insurgents. GAME OVER!!!.")
else:
     print("Wrong command")

if choice3 == "1"   :
    print("YOU WIN")
elif choice3 == "2" or "3":
    print("Not the best choice. GAME OVER")
else:
    print("Time has run out")


# 
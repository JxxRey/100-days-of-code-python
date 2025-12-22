from token import LEFTSHIFT

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You wake up in the middle of a desert!!")
path_1 = input('Lost, you must choose a direction to start walking, do you choose "left" or "right"? ').lower()
if path_1 == "left":
    print("You begin walking left, after a couple minutes quicksand sucks you into the ground.")
    print("You find yourself in some sort of underground tunnel.")
    path_2 = input("In the cave you find a crossbow, suddenly you see lara croft swimming toward you with an alligator chasing her,"
                   " do you shoot the alligator and save her? yes or no ")
else:
    print("You take a couple steps right and a venomous snake comes out behind a rock and bites you.")
    print("GAME OVER")
if path_2 == "yes":
    print("You shoot the crossbow at the alligator, you miss but lara makes it out anyways.")
    print("While making the excuse of just having ate popcorn so your hands were buttery causing your finger to slip"
          "you and lara walk down a narrow path leading to 3 different colored doors.")
    path_3 = input("Choose a colored door. red, blue or yellow.")
else:
    print("You miss and accidentally shoot lara, woops. The alligator then eats you.")
    print("GAME OVER")
if  path_3 == "red":
    print("You open the door of fire, a giant skeleton mage hurls a fireball at you and you get incinerated."
          "GAME OVER")
elif path_3 == "blue":
    print("You open the door of ice, a giant skeleton mage hurls an iceball at you freezing you to death."
          "GAME OVER")
elif path_3 == "yellow":
    print("You open the door of wealth, on a pedestal is a priceless artifact worth millions, lara grabs it and runs away with it never to be seen again, but you survive and make it back home.")
    print("YOU WIN")
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

direction = input("""You are standing at a crossroad.\n 
Before you is a dark forest. The road continues to the left and the right.\n 
Home is behind you. Choose your path: Left or Right? (L/R) """)
if direction == "L":
    print("""You have come to a great body of water.\n 
It is such a hot day, you dip your handkerchief into the cool water and place it on the back of your neck\n""")
    boat = input("You see a small island in the distance. Do you wait for the boat to come back or do you swim? (W/S) ")
    if boat == "W":
        print("You arrive on the island unharmed.\n")
    else:
        print("""You are attacked by something in the deep, cold waters.\n 
The light fades quickly as you sink to the murky depths.\n 
Just before you drown, you feel razor sharp teeth. . . """)

    door = input("""You arrive on the island to find a Giant's Castle in the center.
The Castle has three gates.\n
Which gate do you enter; The Blue gate, the Red gate, or the Yellow gate? (B/R/Y) """)
    if door == "B":
        print("As you step into the gloom just past the Blue gate, you do not see the open oubliette at your feet."
              " No one hears your screams as you plunge ever down into the darkness. . . ")
    elif door == "R":
        print("""In your haste to find shade you assume the gate is hot because of the strong sunshine of the day\n. 
It is not until you open it that you realize your mistake. Behind the Red Gate a fire roars and cracks\n.
Your charred and twisted body is never found. . . """)
    elif door == "Y":
        print("""You have found the Giant's treasure! Fill your pockets quickly before he grinds your bones to make
the bread!""")
    else:
        print("You chose a door that does not exist. Game over!")
else:
    print("You wonder for days down the seemingly endless road. The hot, humid forest road gives way to hot, dry "
          "desert winds. Many years later, your bleached bones grin up at the merciless sun.")


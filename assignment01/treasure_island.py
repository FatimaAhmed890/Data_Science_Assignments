def treasure_island():
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
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
    print("Welcome to Treasure Island\nYour mission is to find the treasure")

    choice_1 = input("You\'re at a cross road. Where do you want to go? \"left\" or \"right\"\n").lower()

    if choice_1 != "left":
        print("Fall into a hole\nGame Over")
        return
    elif choice_1 == "left":
        choice_2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim accross.\n").lower()
        if choice_2 != "wait":
            print("Attacked by beasts\nGame Over")
            return 
        elif choice_2 == "wait":
            print("You\'ve reached the island unharmed. There is a house with three doors.\n") 
            choice_3 = input("Which door do you want to choose? \"Red\" or \"Blue\" or \"Yellow\" \n").lower()
            if choice_3 == "red":
                print("Burned by fire\nGame Over")
                return
            elif choice_3 == "blue":
                print("Eaten by beasts\nGame Over")
            elif choice_3 == "Yellow":
                print("You Win!")
                return
            else:
                print("Game Over")
                return 

if __name__ == "__main__":      
    treasure_island()
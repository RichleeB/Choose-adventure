print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")
option1 = input(
    "At a crossroad. Do you go left or right? Type 'left or 'right': ")
if option1 == "left":
    option2 = input(
        "You find a lake.Do you wait for a boat or swim across? Type 'wait'or 'swim': "
    )
    if option2 == "wait":
        option3 = input(
            " Which gate will you enter? Type: 'first', 'second', or 'third'. "
        )
        if option3 == "first":
            print(
                '''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''
            )
            print("You found the treasure!! You win!")
        elif option3 == "second":
            print(
                "Soon after you enter the gate a dragon appears.It ends quickly. Game Over."
            )
        else:
            print(
                "You step through the gate only to feel the ground beneath you give way. It's a long way down. Game Over."
            )

    else:
        print(
            "Dark shapes appear in the water around you. Something brushes against you..then you feel the force of teeth sink into you as you are pulled under. Game Over."
        )
else:
    print(
        "As you traverse through a rocky path you feel a sharp pain in your ankle. You look down, catch a glimpse of a viper,and realize you've been bitten. You won't make it very far. Game Over. "
    )

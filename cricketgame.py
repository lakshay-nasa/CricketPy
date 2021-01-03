#cricket game

import random

class Game_root:
    pass


class Comp(Game_root):
    def __init__(self,num):
        self.num = num

    def randnum(self):
        return self.num
    
    def __str__(self):
        print(self.num)

class Player(Game_root):
    def __init__(self,name):
        self.name = name
        print("Welcome,",self.name)

    def choose_level(self,level = 1):
        level = int(input("Choose your level--> 1 or 2 : "))
        self.level = level
        print(f"Level = {self.level}")

    def game_start(self):
        try:
            input("Press Enter to continue...")
        except SyntaxError:
            print("Try again....****", input("Press Enter to continue...") , "***")

        else:
            print("Starting game...")
            print(3)
            print(2)
            print(1)
            print("GO")



player_name = (input("Enter your name: "))

Player1 =  Player(player_name)
Player1.choose_level()

if Player1.choose_level == 1:
    random_number = random.randint(1,5)

else:
    random_number = random.randint(1,10)

Comp1 = Comp(random_number)



Player1.game_start()

while True:
    try:
        player_show = int(input("Enter number 1 to 5 : "))
    except Exception as e:
        print("Enter valid number")

    else:
        print(f"Computer choosed -->{Comp1.randnum()}\n")
        print(f"{player_name} choosed --> {player_show}")




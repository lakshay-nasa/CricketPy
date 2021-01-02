#cricket game

import random

class comp:
    def __init__(self,num):
        self.num = num
        # print(self.num)
        # self.level = level
        # print("Your level", self.level)
    def randnum(self):
        print(self.num)

class Player:
    def __init__(self,name):
        self.name = name
        print("Welcome,",self.name)

    
# print(random.randint(1,10))

# class Greet:

player_name = (input("Enter your name: "))
# player_level = (int(input("choose your level: ")))

random_number = random.randint(1,10)

Comp1 = comp(random)
Player1 =  Player(player_name)

# Player1.greet(user_name)



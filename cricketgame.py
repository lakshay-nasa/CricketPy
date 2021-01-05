#cricket game

import random

class Game_root:
    pass

class Comp(Game_root):
    def __init__(self,num):
        self.num = num

    def randnum(self):
        return self.num

class Player(Game_root):
    def __init__(self,name):
        self.name = name
        print("Welcome,",self.name)

    def choose_level(self,level = 1):   
        try:
            level = int(input("Choose your level--> 1 or 2 : "))

        except ValueError:
            if level == 1:
                pass
            else:
                print('Enter valid value')
        
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


def cointoss(tossChoosed):
    coin = random.randint(1,2)
    # print(coin)

    if coin == 1:
        coin = 'h'  #(Head)
    
    elif coin == 2:
        coin = 't'   #(Tail)

    if coin == tossChoosed:
        tosswin = True
        print('You got Batting')
    else:
        tosswin = False
        print('You got Bowling')
    return tosswin


print("Cricket Game")

player_name = (input("Enter your name: "))
Player1 =  Player(player_name)

toss_input = input("***Choose Head(H) OR Tail(T)***")
toss_result = cointoss(toss_input)

Player1.choose_level()
choosed_level = Player1.level

if choosed_level == 1:
    random_number = random.randint(1,5)
    maxNum = 5

elif choosed_level == 2:
    random_number = random.randint(1,10)
    maxNum = 10

else:
    print("Enter valid value")



Comp1 = Comp(random_number)
rand_num = Comp1.randnum()

Player1.game_start()

player_num = None
player_score = 0
comp_score = 0

if toss_result == True: # if player got batting.
    while player_num != rand_num:
        rand_num = random.randint(1,random_number)
        print(rand_num)
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\nComputer choosed -->{rand_num}")
            print(f"{player_name} choosed --> {player_num}")
            if player_num is not rand_num:
                player_score += player_num
            else:
                pass

    print("Your batting score is", player_score)
    print("Now Computer's Turn")


    # toss_result = False     # After player turn is over
    rand_num = None
    while player_num != rand_num:
        rand_num = random.randint(1,random_number)
        print(rand_num)
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\nComputer choosed -->{rand_num}")
            print(f"{player_name} choosed --> {player_num}")
            if player_num is not rand_num:
                comp_score += rand_num
            else:
                pass
    print("Computer Score is", comp_score)
        

elif toss_result == False: # if player got bowling
    while player_num != rand_num:
        rand_num = random.randint(1,random_number)
        print(rand_num)
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\nComputer choosed -->{rand_num}")
            print(f"{player_name} choosed --> {player_num}")
            if player_num is not rand_num:
                comp_score += rand_num
            else:
                pass
    print("Computer Score is", comp_score)
    print("Now your's Turn")

    # toss_result = True    # when computer turn is over

    rand_num = None
    while player_num != rand_num:
        rand_num = random.randint(1,random_number)
        print(rand_num)
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\nComputer choosed -->{rand_num}")
            print(f"{player_name} choosed --> {player_num}")
            if player_num is not rand_num:
                player_score += player_num
            else:
                pass
    print("Your batting score is", player_score)
            

print(f"Your score is {player_score}\nComputer score is {comp_score}")

if player_score > comp_score:
    print("You Win")

elif player_score == comp_score:
    print("Game Tie") 

else:
    print("You Loose")
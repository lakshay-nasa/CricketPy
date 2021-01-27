# cricket game

import random


class Game_root:
    pass


class Comp(Game_root):
    def __init__(self, num):
        self.num = num

    def randnum(self):
        return self.num


class Player(Game_root):
    def __init__(self, name):
        self.name = name
        print(f"\nWelcome, {self.name}\n")

    def choose_level(self, level=1):
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
            print("Try again....****", input("Press Enter to continue..."), "***")

        else:
            print("Starting game...")
            print(3)
            print(2)
            print(1)
            print("GO")


def cointoss(tossChoosed):
    coin = random.randint(1, 2)
    # print(coin)                                               #--> for testing

    if coin == 1:
        coin = 'H'  # (Head)

    elif coin == 2:
        coin = 'T'  # (Tail)

    if coin == tossChoosed:
        tosswin = True
        print('\n**You got Batting**\n')
    else:
        tosswin = False
        print('\n**You got Bowling**\n')
    return tosswin


print("Cricket Game")

player_name = (input("Enter your name: "))
Player1 = Player(player_name)

play_help = None
play_help_entry_allowed = ['H', 'P']

while play_help not in play_help_entry_allowed:
    play_help = input("***PLAY[P]***    ***HELP[H]***\n")
    play_help = play_help.upper()

    if play_help not in play_help_entry_allowed:
        print('Enter valid value')

    else:
        pass

with open("help.txt") as f:
    help = f.read()

if play_help == 'H':
    print(help)

else:
    pass


toss_input = None
toss_entry_allowed = ['H', 'T']

while toss_input not in toss_entry_allowed:
    toss_input = input("\n***Choose Head(H) OR Tail(T)***\n")
    toss_input = toss_input.upper()

    if toss_input not in toss_entry_allowed:
        print("Enter valid value")
    else:
        pass

toss_result = cointoss(toss_input)

Player1.choose_level()
choosed_level = Player1.level

if choosed_level == 1:
    random_number = random.randint(1, 5)
    maxNum = 5

elif choosed_level == 2:
    random_number = random.randint(1, 10)
    maxNum = 10

else:
    print("Enter valid value")

Comp1 = Comp(random_number)
rand_num = Comp1.randnum()

Player1.game_start()

player_num = None

player_score = 0
comp_score = 0

# if player got batting.
if toss_result == True:
    while player_num != rand_num:
        rand_num = random.randint(1, maxNum)
        # print(rand_num)                                                               #--> for testing
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\n**Computer choosed -->{rand_num}")
            print(f"**{player_name} choosed --> {player_num}\n")
            if player_num is not rand_num:
                player_score += player_num
            else:
                pass

    print("Your batting score is", player_score)
    print("Now Computer's Turn")

    # toss_result = False                                                    # After player turn is over
    rand_num = None
    while player_num != rand_num:
        rand_num = random.randint(1, maxNum)
        # print(rand_num)                                                               #---> for testing
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\n**Computer choosed -->{rand_num}")
            print(f"**{player_name} choosed --> {player_num}\n")
            if player_num is not rand_num:
                comp_score += rand_num
            else:
                pass
    print("Computer Score is", comp_score)


elif toss_result == False:                                                  # if player got bowling
    while player_num != rand_num:
        rand_num = random.randint(1, maxNum)
        # print(rand_num)                                                               #--> for testing
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\n**Computer choosed -->{rand_num}")
            print(f"**{player_name} choosed --> {player_num}\n")
            if player_num is not rand_num:
                comp_score += rand_num
            else:
                pass
    print("Computer Score is", comp_score)
    print("Now your's Turn")

    # toss_result = True                                                   # when computer turn is over

    rand_num = None
    while player_num != rand_num:
        rand_num = random.randint(1, maxNum)
        # print(rand_num)                                                               #--> for testing
        try:
            player_num = int(input(f"Enter number 1 to {maxNum} : "))

        except Exception as e:
            print("Enter valid number")

        else:
            print(f"\n**Computer choosed -->{rand_num}")
            print(f"**{player_name} choosed --> {player_num}\n")
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

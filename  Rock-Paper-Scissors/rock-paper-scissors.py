# Rock Paper Scissors

import random


def player_won(player, computer):
    if computer in defender[player]:
        return False;
    return True;




def welcome():
    player = input("Enter your name: ")
    print(f'Hello, {player}')
    rating_file = open("rating.txt")

    for line in rating_file:
        line = line.split()
        if line[0] == player:
            player_rating = int(line[1])
            break

    rating_file.close()
    word = ["rock", "paper", "scissors"]
    player_defined_list = input()
    if player_defined_list != "":
        word = player_defined_list.split(',')

    length = len(word)
    for _i in range(length):
        temp= []
        for _k in range(length // 2):
            temp.append(word[(_i + _k + 1) % length])
        defender[word[_i]] = temp
    print("Okay, let's start")
    return word

defender = {}
player = None
player_rating = 0

word = welcome()

while True:
    user = input() # user means user input
    if user == "!exit":
        print("Bye!")
        break
    elif user == "!rating":
        print(f"Your rating: {player_rating}")
        continue
    elif user not in word:
        print("Invalid input")
        continue


    i = random.randrange(len(word))
    computer = word[i]

    if  user == computer:
        print(f"There is a draw ({user})")
        player_rating += 50
    else:
        if player_won(user, computer):
            print(f"Well done. Computer chose {computer} and failed")
            player_rating += 100
        else:
            print(f"Sorry, but computer chose {computer}")


import random

# Python review using conditional statement

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer} ")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "c You win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes sicssors! You lose!"
    

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)



def likes(names):
    list_names = [[], ["Peter"],["Jacob", "Alex"], ["Max", "John", "Mark"], ["Alex", "Jacob", "Mark", "Max"]]
    names = list_names
    for name in names:
        if len(name) == 0:
            return("no one likes this")
        elif len(name) == 1:
            return name[1] + "likes this"
        elif len(name) == 2:
            return " and ".join(names) + "like this"
        elif len(name) == 3:
            return " and " + "and".join(names)+ "like this"
        elif len(name) == 4:
            return("Alex, Jacob and 2 others like this")
    


likes(names=None)


def likes(names=[]):

    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return str(names) + "likes this"
    elif len(names) == 2:
        return " and ".join(names) + "like this"
    elif len(names) == 3:
        return " and " + "and".join(names)+ "like this"
    elif len(names) == 4:
        return "Alex, Jacob and 2 others like this"
    

likes(names)
likes(names(["Peter"]))
likes(names(["Jacob", "Alex"]))
likes(names(["Max", "John", "Mark"]))
likes(names(["Alex", "Jacob", "Mark", "Max"]))
import random
from enum import IntEnum

class Action(IntEnum):
   Rock = 0
   Paper = 1
   Scissors = 2

Moves = {
    Action.Rock:"Rock",
    Action.Paper:"Paper",
    Action.Scissors:"Scissors"
}
def PlayerSelect():
    Player = input("[0] Rock | [1] Paper | [2] Scissors: ")
    Selected = int(Player)
    action = Action(Selected)
    print("You chose: " + Moves.get(action))
    return action

def CPUSelect():
    Selected = random.randint(0, 2)
    action = Action(Selected)
    print("Computer chose: " + Moves.get(action))
    return action
 
def Winner(PlayerSelect, CPUSelect):
    Wins = 0
    Losses = 0
    Draw = 0
    if PlayerSelect == CPUSelect:
        Draw += 1
        print("It's a draw!")
        print("Current draw count: " + str(Draw))
    elif PlayerSelect == Action.Rock:
        if CPUSelect == Action.Scissors:
            Wins += 1
            print("You won!")
            print("Current win count: " + str(Wins))
        else:
            Losses += 1
            print("You lost!")
            print("Current losses count: " + str(Losses))
    elif PlayerSelect == Action.Scissors:
        if CPUSelect == Action.Paper:
            Wins += 1
            print("You won!")
            print("Current win count: " + str(Wins))
        else:
            Losses += 1
            print("You lost!")
            print("Current losses count: " + str(Losses))
    elif PlayerSelect == Action.Paper:
        if CPUSelect == Action.Rock:
            Wins += 1
            print("You won!")
            print("Current win count: " + str(Wins))
        else:
            Losses += 1
            print("You lost!")
            print("Current losses count: " + str(Losses))

while True:
    try:
        PlayerSelect = PlayerSelect()
    except ValueError as e:
        range_str = "[0, 2]"
        print("Invalid selection.")
        continue

    CPUSelect = CPUSelect()
    Winner(PlayerSelect, CPUSelect)

    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != "y":
        break

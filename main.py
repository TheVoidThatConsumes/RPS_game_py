import random

while True:
    hand_sign = input("What would it be? (rock, paper, scissor) ===> ")

    possible_actions = ["rock", "paper", "scissor"]
    ai_yourmove = random.choice(possible_actions)
    print(f"\nYou throw a {hand_sign}, your opponent throws a {ai_yourmove}.\n")

    if hand_sign == ai_yourmove:
        print(f"Both players threw {hand_sign}. It's a tie!")
    
    elif hand_sign == "rock":
        if ai_yourmove == "scissor":
            print("Your Rock breaks your opponent's Scissor. YOU WIN!")
        else:
            print("Your opponent's Paper covers your Rock. YOU LOSE!")
    
    elif hand_sign == "paper":
        if ai_yourmove == "rock":
            print("Your Paper covers your opponent's Rock. YOU WIN!")
        else:
            print("Your opponent's Scissor cuts your Paper. YOU LOSE!")

    elif hand_sign == "scissor":
        if ai_yourmove == "paper":
            print("Your Scissor cuts through your opponent's Paper. YOU WIN!")
        else:
            print("Your opponent Rock breaks your Scissor. YOU LOSE!")



    replay = input("Do you want to try again? (y/n): ")
    if replay.lower() != "y":
        break


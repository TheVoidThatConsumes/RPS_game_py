import random

win_screen_player = ("""        
 __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)                              
            """)

win_screen_cpu = ("""
   _____ _____  _    _  __          ___           _ 
  / ____|  __ \| |  | | \ \        / (_)         | |
 | |    | |__) | |  | |  \ \  /\  / / _ _ __  ___| |
 | |    |  ___/| |  | |   \ \/  \/ / | | '_ \/ __| |
 | |____| |    | |__| |    \  /\  /  | | | | \__ \_|
  \_____|_|     \____/      \/  \/   |_|_| |_|___(_)
            """)




while True:
    hand_sign = input("Pick a Gesture (R, P, S): ")
    hand_sign = hand_sign.upper()

    possible_actions = ["R", "P", "S"]
    ai_yourmove = random.choice(possible_actions)

    

    if hand_sign == ai_yourmove:
        print(f"Both players threw {hand_sign}. It's a tie!")


    
    elif hand_sign == "R":
        if ai_yourmove == "S":
            print("Player (You): Rock")
            print("CPU: Scissor")
            print("Your Rock breaks your opponent's Scissor.")
            print(win_screen_player)

        else:
            print("Player (You): Rock")
            print("CPU: Paper")
            print("Your opponent's Paper covers your Rock.")
            print(win_screen_cpu)
            
        break




    elif hand_sign == "P":
        if ai_yourmove == "R":
            print("Player (You): Paper")
            print("CPU: Rock")
            print("Your Paper covers your opponent's Rock.")
            print(win_screen_player)

        else:
            print("Player (You): Paper")
            print("CPU: Scissor")
            print("Your opponent's Scissor cuts your Paper.")
            print(win_screen_cpu)
        
        break




    elif hand_sign == "S":
        if ai_yourmove == "P":
            print("Player (You): Scissor")
            print("CPU: Paper")
            print("Your Scissor cuts through your opponent's Paper.")
            print(win_screen_player)
        else:
            print("Player (You): Scissor")
            print("CPU: Rock")
            print("Your opponent Rock breaks your Scissor.")
            print(win_screen_cpu)

        break

       


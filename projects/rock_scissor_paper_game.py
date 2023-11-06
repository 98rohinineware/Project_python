import random

L = ["rock", "scissor", "paper"]

print("Welcome to the Game!!!!")

while True:
    user_count = 0
    com_count = 0
    
    uc = int(input("""
    1. Play | Yes
    2. No | Exit
    """))
    
    if uc == 1:
        for i in range(1, 6):    '''this line show howlong code will run'''
            user_input = int(input("""
            1. Rock
            2. Scissor
            3. Paper
            """))

            if user_input == 1:
                result = "rock"
            elif user_input == 2:
                result = "scissor"
            elif user_input == 3:
                result = "paper"

            com_choice = random.choice(L)

            if com_choice == result:
                print("Game Tie")
            elif (result == "rock" and com_choice == "scissor") or (result == "paper" and com_choice == "rock") or (result == "scissor" and com_choice == "paper"):
                print("You win")
                user_count += 1
            else:
                print("Computer win")
                com_count += 1

            print("User input here:", result)
            print("Computer input here:", com_choice)

        if user_count == com_count:
            print("Game draw.....")
        elif user_count > com_count:
            print("You win.....")
        else:
            print("Computer win.....")

        print("User count", user_count)
        print("Computer count", com_count)

    else:
        break


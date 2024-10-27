import random
rock = "rock"
paper = "paper"
scissors = "scissors"
play_to_false = True


while play_to_false:
    player_choise = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_choise == "r":
        player_choise = rock
    elif player_choise == "p":
        player_choise = paper
    elif player_choise == "s":
        player_choise = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1 :
        computer_random_number = rock
    elif computer_random_number == 2:
        computer_random_number = paper
    else:
        computer_random_number = scissors
    print(f"The computer chose {computer_random_number}.")

    if player_choise == rock and computer_random_number == scissors or\
            player_choise == paper and computer_random_number == rock or\
            player_choise == scissors and computer_random_number == paper:
        print("You win!")
    elif player_choise == computer_random_number :
        print("Draw!")
    else:
        print("You lose :(")
    player_continue = input("Choose [Y]es for another game or [N]o to finish the game: ")
    if player_continue == "Y":
        continue
    elif player_continue =="N":
        print("Game finish!")
        play_to_false = False
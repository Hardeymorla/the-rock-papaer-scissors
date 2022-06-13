import random
cpu_wins = 0
player_wins = 0

# player input function
def player_option():
    player_choice = input("choose Rock, Paper, or Scissors: ")
    if player_choice in ['Rock', 'rock', 'R', 'r']:
        player_choice = 'r'
    elif player_choice in ['Paper', 'paper', 'P', 'p']:
        player_choice = 'p'
    elif player_choice in ['Scissors', 'scissors', 'S', 's']:
        player_choice = 's'
    else:
        print("Error! choose another option.")
        player_option()
    return player_choice

# computer input function
def cpu_option():
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        cpu_choice = "r"
    elif cpu_choice == 2:
        cpu_choice = "p"
    else:
        cpu_choice == 's'
        cpu_option()
    return cpu_choice

# comparing the result
while True:
    print("")   #for cosmetics
    player_choice = player_option()
    cpu_choice = cpu_option()
    print("")    #for cosmetics

    # running series of if and elif statements for the coparism
    if player_choice == "r":
        if cpu_choice == "r":
            print("you chose rock. The computer chose rock. you tied.")

        elif cpu_choice == "p":
            print("you chose rock. The computer chose paper. you lose.")
            cpu_wins += 1

        elif cpu_choice == "s":
            print("you chose rock. The computer chose scissors. you win.")
            player_wins += 1

    elif player_choice == "p":
        if cpu_choice == "r":
            print("you chose paper. The computer chose rock. you win.")
            player_wins += 1

        elif cpu_choice == "p":
            print("you chose paper. The computer chose paper. you tied.")

        elif cpu_choice == "s":
            print("you chose rock. The computer chose scissors. you lose.")
            cpu_wins += 1

    elif player_choice == "s":
        if cpu_choice == "r":
            print("you chose scissors. The computer chose rock. you lose.")
            cpu_wins += 1

        elif cpu_choice == "p":
            print("you chose scissors. The computer chose paper. you win.")
            player_wins += 1

        elif cpu_choice == "s":
            print("you chose scissorsk. The computer chose scissors. you tied.")
            cpu_wins += 1
    
print("")   # to add a space
print("player wins: " + str(player_wins))
print("cpu wins: " + str(cpu_wins))

while true:
    player_choice = input("do you want to play again? (y/n)")
    if player_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif player_choice in ["N", "n", "no", "No"]:
        break
    else:
        pass
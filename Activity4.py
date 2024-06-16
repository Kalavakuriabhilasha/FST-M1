player1 = input("player 1 name:")
player2 = input("player 2 name:")

player1_choice = input(player1 + ", do you want to choose rock, paper or scissors? ").lower()
player2_choice = input(player2 + ", do you want to choose rock, paper or scissors? ").lower()

if  player1_choice ==  player2_choice:
    print("It's a tie!")
elif  player1_choice == 'rock':
    if  player2_choice == 'scissors':
        print("Rock wins!")
    else:
        print("Paper wins!")
elif  player1_choice == 'scissors':
    if  player2_choice == 'paper':
        print("Scissors win!")
    else:
        print("Rock wins!")
elif  player1_choice == 'paper':
    if  player2_choice == 'rock':
        print("Paper wins!")
    else:
        print("Scissors win!")
else:	
    print("Invalid input! You have not entered rock, paper or scissors, try again.")
secondround = input("Do you want to play another round? Yes/No: ").lower()
if(secondround == "yes"):
    pass
elif(secondround == "no"):
    raise SystemExit
else:
    print("You entered an invalid option. Exiting now.")
raise SystemExit
    
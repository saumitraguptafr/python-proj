#ROCK , PAPER, SCISSORS
import random
options = ("scissor","rock","paper")
comp_points = 0
player_points = 0
while True:
    answer = input("ROCK, PAPER OR SCISSOR? (press q to not play anymore): ").lower()
    power = random.choice(options)
    if answer == "q":
        print("Computer looks forward to playing with u in future!")
        break
    elif answer.isalpha() is not True:
        print("Please choose one from the given option")
    elif answer not in options and answer is not "q":
             print("not valid, try again!")
    elif answer == "rock" and power == "paper":
        print("computer chose paper!")
        print("Computer wins!")
        comp_points += 1
    elif power == "rock" and answer == "paper":
         print("computer chose rock!")
         print("Player wins!")
         player_points += 1
    elif answer == "rock" and power == "scissor":
         print("computer chose scissor!")
         print("Player wins!")
         player_points += 1
    elif answer == "scissor" and power == "rock":
         print("computer chose rock!")
         print("Computer wins!")
         comp_points += 1
    elif answer == "paper" and power == "scissor":
        print("computer chose scissor!")
        print("computer wins!")
        comp_points += 1
    elif answer == "scissor" and power == "paper":
        print("computer chose paper!")
        print("Player wins!")
        player_points += 1
    elif answer == "scissor" and power == "scissor":
         print("computer chose scissor!")
         print("Its a draw")
    elif answer == "paper" and power == "paper":
         print("computer chose paper!")
         print("Its a draw")
    elif answer == "rock" and power == "rock":
         print("computer chose rock!")
         print("Its a draw")

                        
   
print(f"The computer won {comp_points} no of times")
print(f"The player won {player_points} no of times")
if comp_points > player_points:
        print("THE COMPUTER WINS OVERALL!")
elif comp_points == player_points:
     print("Its a draw!")
else:
        print("THE PLAYER WINS OVERALL, CONGRATULATIONS!")
    

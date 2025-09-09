#RPS.py
#Name: Gareth Moodley
#Date: 9-9-2025
#Assignment: Rock Paper Scissors
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  choices = ['R', 'P', 'S']
  computer_choices = [("R", "Rock"), ("P", "Paper"), ("S", "Scissors")]
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  while True:
    #Randomly choose the computer between 'R', 'P', or 'S'
    cpu_choice = computer_choices[random.randint(0, len(computer_choices)-1)] 

    user_choice = input("Select Rock, Paper, or Scissors (R, P, S): ").upper()
    if user_choice not in choices:
        print("Error, please enter R, P, or S")
    else:
        #Determine winner and state what happened to the user
        if cpu_choice[0] == "R" and user_choice == "P":
            print("You win")
            wins += 1
        elif cpu_choice[0] == "R" and user_choice == "S":
            print("You lose")
            losses += 1
        elif cpu_choice[0] == "P" and user_choice == "R":
            print("You lose")
            losses += 1
        elif cpu_choice[0] == "P" and user_choice == "S":
            print("You win")
            wins += 1
        elif cpu_choice[0] == "S" and user_choice == "P":
            print("You lose")
            losses += 1
        elif cpu_choice[0] == "S" and user_choice == "R":
            print("You win")
            wins += 1
        elif cpu_choice[0] == user_choice:
            print("Tie")
            ties += 1
            
        #Ask the user if they would like to play again.
        game_continue = input("Would you like to play again (Y/N): ").upper()
        if game_continue == "N":
            #In the end, print the stats
            print("Wins \t Ties \t Losses")
            print("---- \t ---- \t ------")
            print(wins, "\t", ties , "\t", losses)
            break
        elif game_continue == "Y":
            continue

if __name__ == '__main__':
  main()

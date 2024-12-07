
import random

computer = random.randint(1,3)

#user = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
user = input("Enter Rock, Paper or Scissors: ")

if user == "Rock" or "rock":
    user = 1
if user == "Paper" or "paper":
    user = 2
if user == "Scissors" or "scissors":
    user == 3

#border

if computer == user:
    print("It's a tie! Computer entered",computer)
elif computer == 1 and user == 3:
    print("Computer wins! Computer entered",computer)
elif computer == 2 and user == 1:
    print("Computer wins! Computer entered",computer)
elif computer == 3 and user == 2:
    print("Computer wins! Computer entered",computer)
else:
    print("You win! Computer entered",computer)


#if computer == 1:
  #computer = "Rock"
#if computer == 2:
    #computer = "Paper"
#if computer == 3:
    #computer == "Scissors"
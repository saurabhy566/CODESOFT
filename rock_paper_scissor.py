

import random

options = ("rock","paper","scissor")
playing =True

while playing:
     player = None
     computer = random.choice(options)

     while player not in options:
       player = input("Enter a choice(rock,paper,scissor): ")


       print(f"Player:{player}")
       print(f"computer:{computer}")

       if player==computer:
          print("Its a Tie!")
       elif player =="rock" and computer =="scissor":
          print("Rock smashes scissor! Player wins!")
       elif player =="paper" and computer =="rock":
          print("Paper covers rock! Player wins!")
       elif player =="scissor" and computer =="paper":
          print("Scissor cuts paper! Player wins!")
       else:
          print("You lose!")


       play_again = input("Play again? (yes/no): ") .lower()
       if not play_again =="yes":
           playing = False
print("Thanks for playing")


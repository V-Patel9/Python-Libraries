#import random module
import random

#generate random number between 1 and 3
num = random.randint(1,3)

#get computer_choice from random number
if num==1:
computer_choice = 'rock'
elif num==2:
computer_choice = 'paper'
else:
computer_choice = 'scissors'
  
  
#prompt user to enter choice
user_choice = input("Enter your choice of 'rock','paper','scissors': ")

#generate computer choice again if its same as user choice
while computer_choice==user_choice:
num = random.randint(1,3)
if num==1:
computer_choice = 'rock'
elif num==2:
computer_choice = 'paper'
else:
computer_choice = 'scissors'
  
#print computer choice
print("Computer's choice is",computer_choice)


#validate the rules and get the result from rock,paper and scissors choice
if (user_choice =="rock" and computer_choice=="scissors") or (computer_choice =="rock" and user_choice=="scissors"):
print("Rock smashes the scissors.Rock wins!!")
result = "rock"
  
elif (user_choice =="scissors" and computer_choice=="paper") or (computer_choice =="scissors" and user_choice=="paper"):
print("Scissors cuts paper.Scissors wins!!")
result = "scissors"
  
else:
print("Paper wraps rock.Paper wins!!")
result = "paper"
  
#if result is computer_choice , computer wins
if result==computer_choice:
print("Computer wins!!")
else:
#else user wins
print("User wins!!")
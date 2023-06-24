import random


print(".............welcome to RPS.............")

user_score=0
comp_score=0
ties=0

name= input ("Enter your name here:")
print("""
winning Rules:
1.Paper vs Rock--> Paper  
2.Rock vs Scissor-->Rock
3.Scissor vs Paper--> Scissor
"""
 )
print()
while True:
  print(""" choice are:
  1.Rock
  2.Paper
  3.Scissor""")
  choice=int(input("enter your choice from 1-3:"))
  print()
  while choice>3 or choice<1:
    choice=int(input("enter valid input"))
  if choice ==1:
    user_choice="Rock"
  elif choice==2:
    user_choice="Paper"
  else:
    user_choice="Scissor"        


  print("The user choice is", user_choice)
  print("Now it is computer's turn")
  computer =random.randint(1,3)
  if computer ==1:
    comp_choice="Rock"
  elif computer==2:
    comp_choice="Paper"
  else:
    comp_choice="Sicssor"
  print("The computer's choice is",comp_choice)    

  if((user_choice=="Paper" and comp_choice=="Rock")or (user_choice =="Rock"and comp_choice=="Paper")):
    print("Paper wins")
    result="Paper"
  elif((user_choice=="Sicssor" and comp_choice=="Rock")or(user_choice=="Rock" and comp_choice=="Sicssor")):
    print("Rock wins")
    result="Rock"
  elif(user_choice==comp_choice):
   print("it's a tie")
   result="tie"
  else:
    print("Scissor wins")
    result="Scissor"
  if result=="Tie":
    ties+=1
  elif result==user_choice:
    print("user wins")
    user_score +=1

  else:
    print("computer wins")
    comp_score +=1
  print("Scores are")
  print(name,"score is",user_score)
  print("computer's score is",comp_score)
  print("ties are",ties)
  repeat=input("do you want to play again?")
  if repeat =="No" or repeat=="No":
    break
print("Game over!")


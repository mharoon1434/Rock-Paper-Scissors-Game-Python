import random
choices =["rock", "paper", "scissors"]
print("1- rock \n2- paper \n3- scissors")
user_choice=str(input("Your choice..."))
computer_choice=random.choice(choices)
#tie case 
if computer_choice==user_choice:
    print("It's tie ")
#user win case 
elif(user_choice=="rock" and computer_choice=="scissors"):
    print("User win")
elif(user_choice=="paper" and computer_choice=='rock'):
    print("User win")
elif(user_choice=="scissors" and computer_choice=="paper"):
    print("User win")
#computer win case
elif(computer_choice=='rock' and user_choice=="scissors"):
    print("Computer win")
elif(computer_choice=='paper' and user_choice=="rock"):
    print("Computer win")
elif(computer_choice=='scissors' and user_choice=="paper"):
    print("Computer win")



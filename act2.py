import random

options = ["rock","paper","scissors"]

user_choice = input ("choose rock pap sci: ")

computer_choice = random.choice(options)

print("you choose:", user_choice)
print("computer choose:", computer_choice)

if user_choice == computer_choice:
    print("tiee")
elif user_choice == "rock" and computer_choice == "scissors":
    print("u win")
elif user_choice == "paper" and computer_choice == "sissors":
    print("u win")
elif user_choice == "sissors" and computer_choice =="rock":
    print>("winn")
else:
    print("lost you have lost ")

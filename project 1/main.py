import random

'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = { "s": 1, "w": -1, "g": 0 }
reverseDict = { 1: "Snake", -1: "Water", 0: "Gun" }

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if you == computer:
    print("It's a tie!")
else:
    if( you == 1 and computer == -1) or ( you == -1 and computer == 0) or ( you == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
    print("game over")
    # if( you == 1 and computer == -1):
    #     print("You win!")
    # elif( you == -1 and computer == 1):
    #     print("You lose!")
    # elif( you == -1 and computer == 0):
    #     print("You win!")
    # elif( you == 0 and computer == -1):
    #     print("You lose!")
    # elif( you == 0 and computer == 1):
    #     print("You win!")
    # elif( you == 1 and computer == 0):
    #     print("You lose!")
    
    
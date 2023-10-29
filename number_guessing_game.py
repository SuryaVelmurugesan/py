import random
import os
def play_game():
    list_of_nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    number=random.choice(list_of_nums)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty=='easy':
        count=0
        for attempts in range(10,0,-1):
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))
            count+=1
            if guess == number + 1 or guess == number + 2 or guess == number + 3:
                print("High, but almost close.")
                
            elif guess > number:
                print("Too high.")
                
            elif guess == number - 1 or guess == number - 2 or guess == number - 3:
                print("Low, but almost close.")
                
            elif guess < number:
                print("Too low.")
            if guess != number and count!=10:
                print("Guess again.")
            elif guess == number:
                print(f"You got it! The answer was {number}.")
                break
        if count==10:
            print("You've run out of guesses, you lose.")
    
    elif difficulty=='hard':
        count=0
        for attempts in range(5,0,-1):
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))
            count+=1
            if guess == number + 1 or guess == number + 2 or guess == number + 3:
                print("High, but almost close.")
                
            elif guess > number:
                print("Too high.")
                
            elif guess == number - 1 or guess == number - 2 or guess == number - 3:
                print("Low, but almost close.")
                
            elif guess < number:
                print("Too low.")
            if guess != number and count!=5:
                print("Guess again.")
            elif guess == number:
                print(f"You got it! The answer was {number}.")
                break
        if count==5:
            print("You've run out of guesses, you lose.")

while input("Do you want to play a game of Guessing Number? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()
    
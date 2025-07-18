import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number_to_guess:
            print("low!")
        elif guess > number_to_guess:
            print("high!")
        else:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Please enter a valid integer.")

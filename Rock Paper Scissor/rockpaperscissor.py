import random

emojies = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}
choices = ('r', 'p', 's')

while True:
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'r' for rock, 'p' for paper, or 's' for scissors.")     
    user_choice = input("Enter rock, paper, or scissors (r/p/s): ").lower()
    if user_choice not in choices:
      print("Invalid choice. Please enter 'r', 'p', or 's'.")
      continue 

    computer_choice = random.choice(choices)

    print(f"you chose:  {emojies[user_choice]}")
    print(f"computer chose: {emojies[computer_choice]}")

    if user_choice == computer_choice:
     print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
     (user_choice == 'p' and computer_choice == 'r') or \
     (user_choice == 's' and computer_choice == 'p'):
     print("You win!")
    else:
     print("You lose!")

    should_continue = input("continue ? (y/n): ").lower()
    if should_continue != 'y':
     print("Thanks for playing!")
    break
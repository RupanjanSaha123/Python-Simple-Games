import random 

questions = {
    "What is the keyword to define a function in python?": "def",
    "What data type is used to store True or False values?": "bool",
    "What is the correct file extension for python files?": ".py",
    "Which symbol is used to comment a single line in python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in python?": "for",
    "What is the output of 2 ** 3 in python?": "8",
    "What keyword is used to create a class in python?": "class",
    "What does the len() function do?": "returns the length of an object",
    "What is  the result of 10 //3 in python?": "3",
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions, 1):
        print(f"{idx}. {question}")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = questions[question].strip().lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    print(f"Game Over! Your final score is {score} out of {total_questions}.")

                
if __name__ == "__main__":
    python_trivia_game()
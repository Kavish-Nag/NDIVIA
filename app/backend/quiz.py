import pandas as pd
import random

def load_questions(file_name="questions.csv"):
    return pd.read_csv(file_name, dtype={'question_id': str}) 

def load_options(file_name="options.csv"):
    return pd.read_csv(file_name, dtype={'question_id': str})  

def load_answers(file_name="answers.csv"):
    return pd.read_csv(file_name, header=None).iloc[:, 0].astype(str).str.strip().tolist()

def run():
    questions = load_questions()
    options = load_options()
    correct_answers = load_answers()
    score = 0
    print("\nWelcome to the Quiz!")
    input("Press Enter to start...")

    question_indices = list(range(len(questions)))
    random.shuffle(question_indices)

    for i in question_indices:
        row = questions.iloc[i]
        question_id = str(row['question_id']).strip()
        question_text = row['question'].strip()
        
        option_row = options[options['question_id'] == question_id].iloc[0]
        options_list = [option_row['option1'], option_row['option2'], option_row['option3'], option_row['option4']]
        correct_answer = correct_answers[i]

        random.shuffle(options_list)
        print(f"\nQuestion {i+1}: {question_text}")
        for j, option in enumerate(options_list, 1):
            print(f"{j}. {option}")

        while True:
            user_input = input("Your answer (1-4): ").strip()
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                break
            print("Invalid input. Please enter a number between 1 and 4.")

        user_choice = options_list[int(user_input) - 1].strip()

        if user_choice == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}")

        input("Press Enter for the next question...")

    print("\nQuiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")

run()
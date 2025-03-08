import pandas as pd

ques = pd.read_csv("questions.csv", header=None).values.tolist()
ans = pd.read_csv("answers.csv", header=None).values.tolist()
admin_info = pd.read_csv("admin_info.csv")
print("Hello Admin, Welcome to NDIVIA Quiz.")

def display_questions():
    if not ques:
        print("\nNo questions available.")
    else:
        print("\nQuestions:")
        for i, q in enumerate(ques, start=1):
            print(f"{i}. {q[0]}")

def display_answers():
    if not ans:
        print("\nNo answers found.")
    else:
        print("\nAnswers:")
        for i, a in enumerate(ans, start=1):
            print(f"{i}. {a[0]}")

def login():
    print("LOGIN")
    user = input("Enter your username: ").strip()

    if user in admin_info['user'].values:
        password = input("Enter your password: ").strip()
        correct_password = admin_info.loc[admin_info['user'] == user, 'password'].values[0]
        if password == correct_password:
            print("Login successful.")
            modify()
        else:
            print("Incorrect password.")
            login()
    else:
        print("Incorrect username.")
        login()

def save_questions(ques):
    df = pd.DataFrame(ques)
    df.to_csv("questions.csv", header=False, index=False)

def save_answers(ans):
    df = pd.DataFrame(ans)
    df.to_csv("answers.csv", header=False, index=False)

def modify():
    while True:
        print("\nAdmin Panel:")
        print("1. View Questions")
        print("2. Add Question")
        print("3. Modify Question")
        print("4. Delete Question")
        print("5. View Answer Key")
        print("6. Modify Answer")
        print("7. Logout")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == 1:
            display_questions()
        elif ch == 2:
            question = input("Enter the new question: ").strip()
            if question:
                answer = input("Enter the answer for this question: ").strip()
                if answer:
                    ques.append([question])
                    ans.append([answer])
                    save_questions(ques)
                    save_answers(ans)
                    print("Question and answer added successfully!")
                else:
                    print("Answer cannot be empty.")
            else:
                print("Question cannot be empty.")
        elif ch == 3:
            display_questions()
            try:
                index = int(input("Enter the question number to modify: ")) - 1
                if 0 <= index < len(ques):
                    new_question = input("Enter the new question text: ").strip()
                    new_answer = input("Enter the new answer text: ").strip()
                    if new_question and new_answer:
                        ques[index] = [new_question]
                        ans[index] = [new_answer]
                        save_questions(ques)
                        save_answers(ans)
                        print("Question and answer modified successfully!")
                    else:
                        print("Question and answer cannot be empty.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
        elif ch == 4:
            display_questions()
            try:
                index = int(input("Enter the question number to delete: ")) - 1
                if 0 <= index < len(ques):
                    ques.pop(index)
                    ans.pop(index)
                    save_questions(ques)
                    save_answers(ans)
                    print("Question and its answer deleted successfully!")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
        elif ch == 5:
            display_answers()
        elif ch == 6:
            display_answers()
            try:
                index = int(input("Enter the question number to modify its answer: ")) - 1
                if 0 <= index < len(ans):
                    new_ans = input("Enter the new answer text: ").strip()
                    if new_ans:
                        ans[index] = [new_ans]
                        save_answers(ans)
                        print("Answer modified successfully!")
                    else:
                        print("Answer cannot be empty.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
        elif ch == 7:
            print("Logging out...")
            return
        else:
            print("Invalid choice, please select again.")

login()

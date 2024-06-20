print("Welcome to my Quiz game")

question_blocks = [
    {"Q1": "What is the output of the following program?\na = 'pythonpandas'\nb = 10\nprint(a+b)", "Answer": "D"},
    {"Q2": "Who developed the Python programming language?", "Answer": "C"},
    {"Q3": "What will be the output of the following python code?\nx = 'abcd'\nfor i in x:\n    print(i.upper())", "Answer": "D"},
]

options = [
    ["A. Pythonpandas10", "B. 10pythonpandas", "C. Pythonpandas", "D. Error"],
    ["A. Wick van Rossum", "B. Rasmus Lerdorf", "C. Guido van Rossum", "D. Niene Stom"],
    ["A. aBCD", "B. abcd", "C. error", "D. ABCD"]
]

score = 0

def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_blocks)):
    question = question_blocks[question_num]
    for key in question:
        if key != "Answer":
            print(f"{key}: {question[key]}")
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your answer (A/B/C/D): ").upper()
    is_correct = check_answer(guess, question["Answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
    print(f"The correct Answer is {question['Answer']}")
    print()

print(f"Your final score is {score}")
print(f"Your score is {(score/len(question_blocks))*100}%")
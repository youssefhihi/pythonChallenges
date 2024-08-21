import random

def quizGame():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": {"A": "Paris", "B": "Berlin", "C": "London", "D": "Rome"},
            "answer": "A",
        },
        {
            "question": "What is the capital of Germany?",
            "options": {"A": "Paris", "B": "Berlin", "C": "London", "D": "Rome"},
            "answer": "B",
        },
        {
            "question": "What is the capital of Italy?",
            "options": {"A": "Paris", "B": "Berlin", "C": "London", "D": "Rome"},
            "answer": "D",
        },
        {
            "question": "What is the capital of Spain?",
            "options": {"A": "Paris", "B": "Berlin", "C": "Madrid", "D": "Rome"},
            "answer": "C",
        },
        {
            "question": "What is the capital of Portugal?",
            "options": {"A": "Lisbon", "B": "Berlin", "C": "Madrid", "D": "Rome"},
            "answer": "A",
        },
        {
            "question": "What is the capital of Switzerland?",
            "options": {"A": "Paris", "B": "Berlin", "C": "Zurich", "D": "Rome"},
            "answer": "C",
        },
        {
            "question": "What is the capital of Austria?",
            "options": {"A": "Vienna", "B": "Berlin", "C": "Zurich", "D": "Rome"},
            "answer": "A",
        },
    ]
    
    result = 0
    incorrectAnswer = []
    random.shuffle(questions)

    for question in questions:
        print(" ----------------------------------------------------- ")
        print(question["question"])
        for option, answer in question["options"].items():
            print(f"{option}) {answer}")
        
        while True:
            answer = input("Enter your answer (A, B, C, D): ").upper()
            if answer in question["options"]:
                break
            print("Invalid option. Please enter A, B, C, or D.")
        
        if answer == question["answer"]:
            result += 1
        else:
            incorrectAnswer.append(question)
    
    print(f"\nYour score is {result} out of {len(questions)}")

    if incorrectAnswer:
        print("\nIncorrect Answers:")
        for question in incorrectAnswer:
            print(question["question"])
            print(f"Correct answer is {question['options'][question['answer']]}")
    else:
        print("**********************************************************")
        print("Congratulations! You answered all questions correctly. ")
        print("**********************************************************")

if __name__ == "__main__":
    quizGame()

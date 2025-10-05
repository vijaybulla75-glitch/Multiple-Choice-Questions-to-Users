def run_quiz(questions):
    score = 0
    print("Welcome to the Quiz!\n")

    for idx, q in enumerate(questions, start=1):
        print(f"Question {idx}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        while answer not in ['A', 'B', 'C', 'D']:
            answer = input("Invalid choice. Please enter A, B, C, or D: ").strip().upper()

        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
            "answer": "C"
        },
    ]

    run_quiz(quiz_questions)

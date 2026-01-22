def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "correct": 2,
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "correct": 1,
        },
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correct": 1},
        {
            "question": "Who wrote Romeo and Juliet?",
            "options": ["Jane Austen", "Shakespeare", "Mark Twain", "Dickens"],
            "correct": 1,
        },
        {
            "question": "What is the largest ocean?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "correct": 3,
        },
    ]

    score = 0
    print("Welcome to the Quiz Game!\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for j, option in enumerate(q["options"]):
            print(f"  {j}: {option}")

        while True:
            try:
                answer = int(input("Your answer (0-3): "))
                if 0 <= answer <= 3:
                    break
                print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if answer == q["correct"]:
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer is: {q['options'][q['correct']]}\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()

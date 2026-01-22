import requests
import html
import random


def quiz_game():
    # Ask user for number of questions
    try:
        amount = int(input("How many questions do you want? "))
        if amount < 1:
            print("Invalid number, using default 5.")
            amount = 5
    except ValueError:
        print("Invalid input, using default 5.")
        amount = 5

    # Ask for difficulty
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty or skipped; using any difficulty.")
        difficulty = ""

    # Full category list
    categories = {
        9: "General Knowledge",
        10: "Entertainment: Books",
        11: "Entertainment: Film",
        12: "Entertainment: Music",
        13: "Entertainment: Musicals & Theatres",
        14: "Entertainment: Television",
        15: "Entertainment: Video Games",
        16: "Entertainment: Board Games",
        17: "Science & Nature",
        18: "Science: Computers",
        19: "Science: Mathematics",
        20: "Mythology",
        21: "Sports",
        22: "Geography",
        23: "History",
        24: "Politics",
        25: "Art",
        26: "Celebrities",
        27: "Animals",
        28: "Vehicles",
        29: "Entertainment: Comics",
        30: "Science: Gadgets",
        31: "Entertainment: Japanese Anime & Manga",
        32: "Entertainment: Cartoon & Animations",
    }

    print("\nAvailable Categories:")
    for id, name in categories.items():
        print(f"{id}: {name}")

    try:
        category_id = int(input("Enter category ID (or leave blank for any): ") or 0)
        if category_id not in categories:
            print("Invalid category, using any category.")
            category_id = 0
    except ValueError:
        print("Invalid input, using any category.")
        category_id = 0

    # Build API URL
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    if difficulty:
        url += f"&difficulty={difficulty}"
    if category_id:
        url += f"&category={category_id}"

    response = requests.get(url)
    data = response.json()

    if data.get("response_code") != 0:
        print("No results found. Using default settings (5 random questions).")
        url = "https://opentdb.com/api.php?amount=5&type=multiple"
        data = requests.get(url).json()

    questions = []
    for item in data["results"]:
        options = item["incorrect_answers"]
        correct_answer = item["correct_answer"]
        options.append(correct_answer)
        random.shuffle(options)

        questions.append(
            {
                "question": html.unescape(item["question"]),
                "options": [html.unescape(opt) for opt in options],
                "correct": options.index(correct_answer),
            }
        )

    score = 0
    print("\nWelcome to the Quiz Game!\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for j, option in enumerate(q["options"]):
            print(f"  {j}: {option}")

        while True:
            try:
                answer = int(input("Your answer (0-3): "))
                if 0 <= answer < len(q["options"]):
                    break
                print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if answer == q["correct"]:
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! Correct answer: {q['options'][q['correct']]}\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()

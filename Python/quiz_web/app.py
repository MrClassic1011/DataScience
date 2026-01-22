from flask import Flask, render_template, request
import requests
import html
import random

app = Flask(__name__)

# Full category list for the dropdown in index.html
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


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = int(request.form.get("amount", 5))
        difficulty = request.form.get("difficulty", "")
        category_id = int(request.form.get("category", 0))

        # Build API URL
        url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
        if difficulty:
            url += f"&difficulty={difficulty}"
        if category_id:
            url += f"&category={category_id}"

        response = requests.get(url)
        data = response.json()

        questions = []
        # Check if API actually returned results
        if data.get("results"):
            for item in data["results"]:
                # Work on a copy of incorrect answers to avoid modifying original API data
                options = list(item["incorrect_answers"])
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

        return render_template("quiz_all.html", questions=questions)

    return render_template("index.html", categories=categories)


if __name__ == "__main__":
    app.run()

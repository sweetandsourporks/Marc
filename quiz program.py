def main():
    quiz_data = [ 
        {
            "quiz_no": 1,
            "question": "Who created the Android OS?",
            "option_a": "Apple",
            "option_b": "Microsoft",
            "option_c": "Google",
            "option_d": "Facebook",
            "correct_answer": "Google",
            "point": 1
        },
        {
            "quiz_no": 2,
            "question": "Who created the Python programming language?",
            "option_a": "Guido van Rossum",
            "option_b": "Bill Gates",
            "option_c": "Steve Jobs",
            "option_d": "Grace Hopper",
            "correct_answer": "Guido van Rossum",
            "point": 1
        },
        {
            "quiz_no": 3,
            "question": "Who is considered the first programmer?",
            "option_a": "Guido van Rossum",
            "option_b": "Bill Gates",
            "option_c": "Ada Lovelace",
            "option_d": "Grace Hopper",
            "correct_answer": "Ada Lovelace",
            "point": 1
        }
    ]

    score = 0
    start_quiz = input("Do you want to start the quiz? (y/n): ")

    if start_quiz.lower() == "y":
        for q in quiz_data:
            print(f"Question No: {q['quiz_no']}")
            print(f"Question: {q['question']}")
            print(f"A: {q['option_a']}")
            print(f"B: {q['option_b']}")
            print(f"C: {q['option_c']}")
            print(f"D: {q['option_d']}", end="\n\n")

            response = input("What is your answer? (a, b, c, d): ").lower()

            if response == "a" and q["option_a"] == q["correct_answer"]:
                score += q["point"]
            elif response == "b" and q["option_b"] == q["correct_answer"]:
                score += q["point"]
            elif response == "c" and q["option_c"] == q["correct_answer"]:
                score += q["point"]
            elif response == "d" and q["option_d"] == q["correct_answer"]:
                score += q["point"]
            else:
                print("Incorrect answer.")

        return score
    else:
        print("Exiting the quiz.")
        return 0

if __name__ == '__main__':
    print("Welcome to my quiz program!")
    name_input = input("Enter your name: ")
    course_input = input("Enter your course: ")
    total_score = main()
    print(f"Your score is {total_score}")
    print("Thank you for playing!")

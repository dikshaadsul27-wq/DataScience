# student_grade.py

def calculate_grade(marks):
    """Return grade and encouraging message based on marks."""
    if 90 <= marks <= 100:
        return "A", "Excellent work! You're a star! 🌟"
    elif 80 <= marks < 90:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks < 80:
        return "C", "Good effort! You can aim higher! 💪"
    elif 60 <= marks < 70:
        return "D", "Fair attempt! Keep practicing! 📘"
    else:
        return "F", "Don’t give up! Learn from mistakes and try again! 🚀"


def get_valid_marks():
    """Prompt user until valid marks (0-100) are entered."""
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid input. Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def main():
    student_name = input("Enter student name: ")
    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR {}:".format(student_name.upper()))
    print("Marks: {}/100".format(marks))
    print("Grade:", grade)
    print("Message:", message)


if __name__ == "__main__":
    main()
def get_grade(score):
    if 70 <= score <= 100:
        return 'A'
    elif 60 <= score <= 69:
        return 'B'
    elif 50 <= score <= 59:
        return 'C'
    elif 45 <= score <= 49:
        return 'D'
    elif 40 <= score <= 44:
        return 'E'
    elif 0 <= score <= 39:
        return 'F'
    else:
        return 'Invalid score. Please enter a score between 0 and 100.'

try:
    score = int(input("Enter your score (0-100): "))
    grade = get_grade(score)
    print(f"Your grade is: {grade}")
except ValueError:
    print("Invalid input. Please enter a number.")

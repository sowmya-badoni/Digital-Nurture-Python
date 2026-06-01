def assign_grade(score):

    if not isinstance(score, (int, float)):
        print("Invalid score")
        return

    if score < 0 or score > 100:
        print("Score should be between 0 and 100")
        return

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    else:
        grade = "C"

    print(f"Score: {score}")
    print(f"Grade: {grade}")


score = 88

assign_grade(score)
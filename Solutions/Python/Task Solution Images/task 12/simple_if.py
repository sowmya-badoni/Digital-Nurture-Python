def check_result(marks):

    if not isinstance(marks, (int, float)):
        print("Invalid marks")
        return

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100")
        return

    if marks >= 40:
        print("Pass")


marks = 75

check_result(marks)
def add(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Error: Both inputs must be numerical values.")
        return None

    return num1 + num2


result = add(5, 3)
print(result)
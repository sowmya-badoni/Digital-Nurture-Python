def countdown(start_value):
    if not isinstance(start_value, int) or start_value <= 0:
        print("Invalid count value. Please provide a positive integer.")
        return

    count = start_value
    while count > 0:
        print(f"Current count: {count}")
        count -= 1


countdown(5)
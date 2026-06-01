def print_numbers(count):

    if not isinstance(count, int) or count <= 0:
        print("Invalid loop count")
        return

    for i in range(5):
        print(i + 1)


print_numbers(5)
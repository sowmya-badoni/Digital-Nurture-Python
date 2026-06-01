def find_first_even(limit):

    if not isinstance(limit, int) or limit <= 0:
        print("Invalid range")
        return

    for i in range(limit):

        if i % 2 == 0:
            print(f"First even number: {i}")
            break


find_first_even(10)
def sum_odd_numbers(max_range):
    if not isinstance(max_range, int) or max_range <= 0:
        print("Error: Range must be a positive integer.")
        return None

    total_sum = 0
    for num in range(max_range):
        if num % 2 == 0:
            continue
        total_sum += num

    print(f"The sum of odd numbers in range({max_range}) is: {total_sum}")
    return total_sum


sum_odd_numbers(10)
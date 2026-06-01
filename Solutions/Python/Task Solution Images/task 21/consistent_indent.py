def check_nested_conditions(condition_one, condition_two):
    if condition_one is True:
        if condition_two is True:
            print("Nested")
            print("Confirmation: Both conditions are verified True.")


check_nested_conditions(True, True)
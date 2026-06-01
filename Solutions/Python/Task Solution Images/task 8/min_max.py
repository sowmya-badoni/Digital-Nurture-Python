def find_salary_range(salaries):

    if not salaries:
        print("Salary list is empty")
        return

    for salary in salaries:
        if not isinstance(salary, (int, float)):
            print("Invalid salary value")
            return

    lowest_salary = min(salaries)
    highest_salary = max(salaries)

    print(f"Lowest Salary: {lowest_salary}")
    print(f"Highest Salary: {highest_salary}")


salary_list = [50000, 75000, 62000, 95000]

find_salary_range(salary_list)
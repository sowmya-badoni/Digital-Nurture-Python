def calculate_area(length, width):

    if length <= 0 or width <= 0:
        return "Invalid dimensions"

    area = length * width

    return area


print(calculate_area(5, 3))
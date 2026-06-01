import math


def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        print("Error: Radius must be a non-negative number.")
        return None

    area = math.pi * (radius**2)
    print(f"The area of the circle is: {area:.2f}")
    return area


calculate_circle_area(5)
# Function to display coordinates
def display_coordinates(coords):

    # Validation
    if len(coords) != 2:
        print("Invalid coordinates")
        return

    # Multiple assignment
    x, y = coords

    # Check datatype
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Coordinates must be numbers")
        return

    # Output
    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")


# Coordinates tuple
point = (10, 20)

# Function call
display_coordinates(point)
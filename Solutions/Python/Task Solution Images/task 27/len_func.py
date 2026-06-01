def get_string_length(text):
    if not isinstance(text, str):
        print("Error: Input must be a string.")
        return None

    length = len(text)
    print(f"The length of the string is: {length}")
    return length


get_string_length("Hello, World!")
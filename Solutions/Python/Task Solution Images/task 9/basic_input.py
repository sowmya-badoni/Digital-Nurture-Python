def greet_user():
    name = input("Enter your name: ").strip()

    if name == "":
        print("Invalid input")
    else:
        print(f"Hello, {name}!")

greet_user()
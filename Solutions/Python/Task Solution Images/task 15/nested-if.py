def validate_login(input_user, input_pwd):
    correct_user = "admin"
    correct_pwd = "pass123"

    if input_user.strip() == "" or input_pwd.strip() == "":
        return "Error: Username or password cannot be blank."
    else:
        if input_user == correct_user:
            if input_pwd == correct_pwd:
                return f"Welcome, {input_user}! Login successful."
            else:
                return "Error: Incorrect password."
        else:
            return "Error: Incorrect username."


username_attempt = input("Enter username: ")
password_attempt = input("Enter password: ")

result = validate_login(username_attempt, password_attempt)
print(result)
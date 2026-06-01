def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None


read_file_content("sample.txt")
def write_message():

    file = open("greeting.txt", "w")

    file.write("Hello World")

    file.close()

    print("Message written to file")


write_message()
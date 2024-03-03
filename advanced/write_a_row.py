def write_to_file():
    with open('file_to_write.txt', 'a') as file:
        text = str(input("Enter text to write into the file: "))
        file.write(text)
        file.close()

write_to_file()
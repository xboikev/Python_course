import os

def f_not_found():
    f_name = "test.txt"
    try:
        file = open(f_name)
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("File not found, check path to file please!!!")

f_not_found()
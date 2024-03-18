import os

def f_not_found():
    f_name = "test.txt"
    try:
        file = open(f_name)
    except FileNotFoundError:
        print("File not found, check path to file please!!!")
    else:
        print(file.read())
        file.close()

f_not_found()
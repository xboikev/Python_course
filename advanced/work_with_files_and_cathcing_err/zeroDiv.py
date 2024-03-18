def zeroDiv():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    try:
        res = x / y
    except ZeroDivisionError:
        print("Second value is null!!!")
        res = 0

    return res

print(zeroDiv())
def to_num():
    fst = input("Enter first num: ")
    snd = input("Enter second num: ")

    try:
        fst = int(fst)
        snd = int(snd)
    except ValueError:
        print("Please, enter the numbers!!!")
    else:
        print("Success!")

to_num()
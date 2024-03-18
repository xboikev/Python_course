def catching_index(elements: list[int]):
    try:
        for i in range(10):
            print(elements[i])
    except IndexError:
        print("Your index is out of boarder, check length of list!!!")
    else:
        print("Success")

catching_index([1,2,3])

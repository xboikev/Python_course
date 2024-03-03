def catching_index(elements: list[int]):
    try:
        for i in range(10):
            print(elements[i])
        print("Success")
    except IndexError:
        print("Your index is out of boarder, check length of list!!!")

catching_index([1,2,3])

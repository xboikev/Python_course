def mult_errors():
    l_of_nums = str(input("Enter list of 10 numbers, separated by comma: ")).split(',')
    try:
        for i in range(10):
            l_of_nums[i] = int(l_of_nums[i])
        print("Success")
    except ValueError:
        print("You've entered not only nums!!!")
    except IndexError:
        print("You've reached the boarders of index, enter the list of following length!!!")
mult_errors()
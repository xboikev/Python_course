def content_diff():
    file1 = open("fst.txt")
    file2 = open("snd.txt")

    for line in file1:
        if line not in file2:
            print(line, end='\n')
    file1.close()
    file2.close()

content_diff()
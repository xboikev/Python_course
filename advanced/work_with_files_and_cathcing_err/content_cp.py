def copy_to_file():
    with open('fst.txt', 'r') as fst_file, open('snd.txt', 'a') as snd_file:
        for line in fst_file:
            snd_file.write(line)

        fst_file.close()
        snd_file.close()

copy_to_file()
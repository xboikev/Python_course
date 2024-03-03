def words_count():
    number_of_words = 0

    with open('fst.txt', 'r') as file:
        text = file.read()
        lines = text.split()
        number_of_words += len(lines)
        file.close()

    print(number_of_words)

words_count()

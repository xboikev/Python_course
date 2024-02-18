import math

def fib(n):
    # n = int(input("Enter the length: "))
    f1 = f2 = 1
    i = 2
    while i < n:
        f1, f2 = f2, f1 + f2
        i += 1
    return f2


def from_sec():
    sec = int(input("Enter amount of seconds: "))
    hours = sec // 3600
    min = sec % 3600 // 60
    print(f" {hours} година\n", f"{min} хвилин\n", f"{sec % 3600 % 60} секунд")


def to_fahr() -> int:
    celsius = int(input("Enter the temperature in celsius: "))
    fahr = int(celsius * (9/5) + 32)
    print(fahr)


def is_even(num:int) -> str:
    print("Парне" if num % 2 == 0 else "Не парне")


def root():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    d = b ^ 2 - 4 * a * c
    if d < 0:
        print("There are no roots")

    elif d == 0:
        print("Root is: ", ((-1) * b) // 2)

    else:
        x1 = int(((-1) * b + math.sqrt(d)) // 2)
        x2 = int(((-1) * b - math.sqrt(d)) // 2)
        print(f"The roots are: \n", x1, "\n", x2)


def the_biggest(fst, snd, thrd):
    return max(fst, snd, thrd)


def r_p_s():
    fst = str(input("Make your choice player1: "))
    snd = str(input("Make your choice player2: "))

    if fst == snd:
        print("Нічия")
    elif fst == "Камінь" or fst == "Ножниці" and snd != "Камінь":
        print("Перший переміг")
    else:
        print("Другий переміг")


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("Високосний")
    else:
        print("Не високосний")


def water_cond(temp):
    if temp <= 0:
        print("Тверда")
    elif temp > 0 and temp < 100:
        print("Рідка")
    else:
        print("Пароподібна")


def days_in_month(m):
    if m == 2:
        return 28
    return 30 if m % 2 == 0 else 31


def calculator():
    fst = int(input("Enter first num: "))
    snd = int(input("Enter second num: "))
    op = input("Enter operation between nums: ")

    match op:
        case '/':
            if snd == 0:
                print("На ноль ділити не можна")
            else:
                return fst // snd
        case '+':
            return fst + snd
        case '-':
            return fst - snd
        case '*':
            return fst * snd


def update():
    fruits = ['яблуко', 'банан', 'апельсин']
    _remove = str(input("Enter name of fruit to be removed: "))
    _add = str(input("Enter name of fruit to be added: "))
    fruits.remove(_remove)
    fruits.append(_add)

    print(fruits)


def substract():
    tuple1 = tuple(input("Enter first tuple: "))
    tuple2 = tuple(input("Enter second tuple: "))
    print(tuple(int(x) for x in tuple1 if x not in tuple2))


def uniq_list(l):
    print(list(set(l)))


def length(l):
    print(len(l))


def union_of_dict(dict1, dict2):
    print(dict1 | dict2)
dict1 = {"ім'я": 'Іван', 'прізвище': 'Петров', 'вік': 25}
dict2 = {'телефон': '123-456-7890', 'email': 'ivan@example.com', 'стать': 'чоловіча'}


def snd_smallest(nums):
    print(list(set(nums))[1])


def vowel_counter(text: str) -> int:
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    count = 0
    for c in text.lower():
        if c in vowels:
            count += 1
    print(count)


def palindrome(text):
    return text.lower() == text.lower()[::-1]


def double_symbol(text):
    new_text = ""
    for i in text:
        new_text += i * 2
    return new_text


def mult_table(num):
    for i in range(11):
        print(f"{num} x {i} = {num * i}")


def FizzBuzz(num):
    init = 1
    while init <= num:
        if init % 3 == 0 and init % 5 != 0:
            print("Fizz")
        elif init % 5 == 0 and init % 3 != 0:
            print("Buzz")
        elif init % 3 == 0 and init % 5 == 0:
            print("FizzBuzz")
        else:
            print(init)
        init += 1


def tree_sum():
    total = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            total += i
    return total


def fact(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


def counter_of_symbols(string):
    res = {}
    for c in string:
        if c not in res:
            res[c] = string.count(c)
    return res


def reverse_of_words(string):
    l = string.split()
    for i in l[::-1]:
        print(i, end=" ")


def sum_(n):
    if n < 0:
        return 0
    total = 0
    while n >= 0:
        total += n
        n = int(input("Enter next number: "))
    return total


def purge(string):
    for word in string.split():
        new_word = ""
        for c in word:
            if c.isalpha():
                new_word += c
        print(new_word, end=" ")


def fst_smallest_num(l):
    return list(set(l))[0]


def enigmatic_num(n):
    correct = 5
    while n != 0:
        if n == correct:
            print("Вітаю ви виграли!")
            break
        n = int(input("Enter new num: "))
    else:
        print("Наступного разу пощастить!")


def mult_by_2(l):
    return [x * 2 for x in l]


def count_vowels(string):
    c = 0
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    for l in string:
        if l in vowels:
            c += 1
    return c


def even_nums(l):
    return [x for x in l if x % 2 == 0]


def reversed_order(string):
    return " ".join(string.split()[::-1])


def to_degree(n1, n2):
    return n1 ** n2


def c_of_all_vowels(w1,w2,w3):
    c_vowels = {}
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    for key in vowels:
        counted_vowels = w1.count(key) + w2.count(key) + w3.count(key)
        if counted_vowels > 0:
            c_vowels[key] = counted_vowels
    return c_vowels


def to_capitalize(string):
    l = [x.capitalize() for x in string.split()]
    return " ".join(l)


def all_to_cap(l):
    return [x.upper() for x in l]


def find_max(l):
    if len(l) == 0:
        return "Пустий список"
    _max = l[0]
    for n in l:
        if n > _max:
            _max = n
    return _max


def is_prime_num(num:int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def fact(num):
    total = 1
    for i in range(2, num + 1):
        total *= i
    return total


def anagrams(w1, w2):
    if len(w1) != len(w2):
        return False
    for c in list(w1):
        if c not in list(w2):
            return False
    return True


def union_of_dicts(dict1, dict2):
    new_dict = dict1.copy()
    for key in dict2:
        if key in dict1:
            new_dict[key] += dict2[key]
        else:
            new_dict[key] = dict2[key]
    return new_dict

dict1 = {'а': 1, 'б': 2, 'в': 3}
dict2 = {'б': 4, 'в': 5, 'г': 6}


def len_of_str(string):
    return len(string.split())

def filter_of_str(l):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    return [word for word in l if len(word) >= 5 and word[0] in vowels]


def endless_line(*args):
    return " ".join(args)

str1 = "Привіт,"
str2 = "як справи?"
str3 = "Доброго дня!"

def counter_words(inputed_string):
    stop_words = ('a', 'але', 'хоча', 'мабудь', 'і', 'та', 'ні')
    filtered_string = inputed_string.lower().replace('.', '').split()
    counted_words = {}
    for word in filtered_string:
        if word not in stop_words and word not in counted_words:
            counted_words[word] = filtered_string.count(word)

    for key in sorted(counted_words, key=counted_words.get, reverse=True):
        print(f"{key}: {counted_words[key]}")


counter_words("І зорі та небо ясне небо. Всі речі прекрасні на землі.")

"""This file contains all of the functions for linting theme."""
import pandas as pd


def calc_sum(fst_num, snd_num):
    """Function that calculates sum of two numbers"""
    if fst_num > 0 and snd_num > 0:
        result = fst_num + snd_num
        return result
    print("Введені числа повинні бути позитивними")
    return None


# Тут використовується лише pandas та json
data = pd.read_json('data.json')
print(data)


from bs4 import BeautifulSoup
import requests
# Тут використовується лише requests та BeautifulSoup
page = requests.get('http://example.com')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


def proc_data(fst_num, sec_num, thrd_num, res):
    # Check if all of numbers greater than 5
    if fst_num > 5 and sec_num > 5 and thrd_num > 5:
        print("All greater than 5")
        return res

    # Else check if some of them less or equal to 5
    if fst_num <= 5 or sec_num <= 5 or thrd_num <= 5:
        print("Some less than or equal to 5")
        return res*2

    return res*3


result = proc_data(3, 6, 9, 12)
print("Result is", result)


def factorial(n):
    """ Функція для обчислення факторіалу """

    # Перевірка типу даних
    if type(n) != int:
        return "Помилка: введіть ціле число"

    if n < 0:
        return "Помилка: число не може бути від'ємним"

    if n == 0:
        return 1

    return n * factorial(n - 1)




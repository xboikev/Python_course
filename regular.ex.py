import re


def without_spaces(text):
    res = re.search('\s', text)
    return "валідний" if res == None else "не валідний"

# print(without_spaces("hello"))


def all_nums(text):
    res = re.search('\D', text)
    return "валідний" if res == None else "не валідний"

# print(all_nums("1928L346"))

def post_indices(text):
    res = re.findall(r'\b\d{5}\b', text)
    return res

# print(post_indices("1928346, фдлц1214, 12345, вв22334, --222--, a12345, 25358, 98q98"))

def date_validation(text):
    res = re.search(r'\b\d{2}\b-\d{2}\b-\d{4}\b', text)
    return "валідна" if res != None else "не валідна"

# print(date_validation("05-05.2025"))

def validation_of_number(text):
    res = re.search("^\\+380 \d{2} \d{3}-\d{4}$", text)
    return "валідний" if res != None else "не валідний"

# print(validation_of_number("+380 99 123-4567"))

def email_check(email):
    res = re.match(r"[a-zA-z^@]+@\w[^@]+\.[^@]+", email)
    return "Valid" if res else "Not valid, please rewrite your email"
# print(email_check("example@f.ua"))
# print(email_check("vladushakov@gmail.com"))

def check_ip(ip):
    res = re.search(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', ip)
    return res.group()

print(check_ip("192.233.255.33"))
import random
import secrets
import string


# Функция генерирует числовые значения 0-9
def generate_random_number_strings(length):
    result = ""
    for i in range(0, length):
        result += str(random.randint(0, 9))
    return result

# Функция генерирует буквенные значения 0-5
def generate_random_letter_strings(length):
    result = ""
    for i in range(0, length):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    return result

# Функция генерирует значение для пароля
def generate_random_password_strings(length):
    result = ""
    for i in range(0, length):
        result += secrets.choice(string.ascii_letters + string.digits)
    return result

# Функция генерирует значение для почты
def generate_random_mail_strings(length):
    result = ""
    for i in range(0, length):
        result += secrets.choice(string.ascii_letters + string.digits)
    return result + "@mail.ru"

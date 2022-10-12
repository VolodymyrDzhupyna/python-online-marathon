# Створити функцію create_account(ім'я_користувача: string, пароль: string, секретні_слова: list). 
# Ця функція повинна повертати внутрішню перевірку функції.
# Функція check порівнює значення своїх аргументів з паролем та секретними словами: 
# пароль повинен співпадати повністю, секретні слова можуть бути написані з помилкою (лише один елемент).
# Пароль повинен містити не менше 6 символів, включаючи одну велику літеру, 
# одну малу літеру, спеціальний символ і одну цифру.
# В іншому випадку функція create_account видасть помилку ValueError. 

# For example: 

# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error 

# If tom = create_account("Tom", "Qwerty1_", ["1", "word"])  

# then 

# tom("Qwerty1_",  ["1", "word"]) return True 

# tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]

# tom("Qwerty1_",  ["word", "12"]) return True

# tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"

# ["abc3", "abc3", "abc3"](check) and ["word1", "abc3", "list"](create_account) --> False
# ["abc3", "word1", "zzzzzz"](check) and ["word1", "abc3", "list"](create_account) --> True
# ["word1", "zzzz", "z"](check) and ["word1", "abc3", "list"](create_account)

import re

def create_account(user_name, password, secret_words):
    result = re.match("^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&!_*+=]).*$", password)
    if not result:
        raise ValueError
    def check(valid_password, check_secret_words):
        lenght_secret_words = len(secret_words)
        lenght_check_secret_words = len(check_secret_words)
        counter = 0
        Flag = True
        for item in secret_words:
            if item in check_secret_words:
                check_secret_words.remove(item)
            else:
                counter += 1
        if counter >= 2:
            Flag = False
        if lenght_secret_words == lenght_check_secret_words and Flag \
                and valid_password == password:
            return True
        return False
    return check

    

tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_",  ["1", "word"]) 
check2 = tom("Qwerty1_",  ["word"]) 
check3 = tom("Qwerty1_",  ["word", "2"]) 
check4 = tom("Qwerty1!",  ["word", "12"])
print(check1)
print(check2)
print(check3)
print(check4)

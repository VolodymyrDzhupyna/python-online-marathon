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

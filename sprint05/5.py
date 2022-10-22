class MyError(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def check_positive(num):
    try:
        if type(num) is str and num.isalpha():
            raise ValueError("ValueError!")
        if float(num) < 0:
            raise MyError(f"You input negative number: {float(num)}. Try again.")
    except MyError as e:
        return e
    except ValueError as e:
        return f"Error type: {e}"
    else:
        return f"You input positive number: {float(num)}"


print(check_positive("6.8"))
print(check_positive(8.9))
print(check_positive(-19))
print(check_positive("abs"))
print(check_positive("45"))
print(check_positive("-235"))

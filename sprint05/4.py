def check_odd_even(num):
    try:
        if type(num) is not int:
            raise ValueError("You entered not a number.")
    except ValueError as e:
        return e
    else:
        return "Entered number is even" if num % 2 == 0 else "Entered number is odd"
    


print(check_odd_even("shf"))
print(check_odd_even(10))
print(check_odd_even(11))
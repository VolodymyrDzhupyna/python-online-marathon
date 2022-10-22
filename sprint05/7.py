def divide(numerator, denominator):
    try:
        return f"Result is {numerator / denominator}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except TypeError:
        return "Value Error! You did not enter a number!"

print(divide(8, 0))
print(divide(16, 8))
print(divide("25", 5))
print(divide("abc", 5))

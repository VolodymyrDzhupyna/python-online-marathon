def morse_number(num):
    DOT_SYMBOL = "."
    DASH_SYMBOL = "-"
    result = ""
    
    for item in num:
        if 0 <= int(item) <= 5:
            result += (int(item) * DOT_SYMBOL) + \
            (5 - int(item)) * DASH_SYMBOL + " "
        elif 6 <= int(item) <= 9:
            result += ((int(item)-5) * DASH_SYMBOL) + \
            (10 - int(item)) * DOT_SYMBOL + " "
    return result.rstrip()


print(morse_number("295"))

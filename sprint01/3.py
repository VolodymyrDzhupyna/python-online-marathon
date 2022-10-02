def isPalindrome(str):
 
    symbol_list = []

    for i in range(len(str)):
        if (str[i] in symbol_list):
            symbol_list.remove(str[i])
        else:
            symbol_list.append(str[i])

    if (len(symbol_list) == 0 or len(symbol_list) == 1):
        return True
    else:
        return False


print(isPalindrome("abcab"))
def order(a):

    flag_descending = False
    flag_ascending = False

    for item in range(1, len(a)):
        if a[item-1] >= a[item]:
            flag_descending = True
        elif a[item] >= a[item-1]:
            flag_ascending = True
        if flag_ascending and flag_descending:
            return "not sorted"

    if flag_descending:
        return "descending"
    if flag_ascending:
        return "ascending"
    
        
print(order([6, 20, 160, 420]))

def studying_hours(a) :

    lenght_a = len(a)
    max_lenght = 1
    current_lenght = 1

    for item in range(1, lenght_a):
        if a[item] > a[item-1] or a[item] == a[item-1]:
            current_lenght += 1
        else:
            if max_lenght < current_lenght:
                max_lenght = current_lenght
            current_lenght = 1

    if max_lenght < current_lenght:
        max_lenght = current_lenght
    return max_lenght
 
 
a = [2, 2, 1, 3, 4, 1]
print(studying_hours(a))
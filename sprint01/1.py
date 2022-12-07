def kthTerm(n, k):
    num_list = [0, 1]
    counter = 1
    while len(num_list) <= k:
        for item in range(len(num_list)):
            num_list.append(n**counter + num_list[item])
        counter += 1
    return num_list[k]


print(kthTerm(10, 99))

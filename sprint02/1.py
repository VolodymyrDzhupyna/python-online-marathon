def double_string(data):
    count = 0
    for item in data:
        if any(item+y in data for y in data):
            count+=1
    return count


data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data))

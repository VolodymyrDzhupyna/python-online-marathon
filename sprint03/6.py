# Функція-генератор randomWord має в якості аргументу список слів. 
# Вона повинна повертати довільне випадкове слово з цього списку. 
# Кожен раз слова будуть різними до тих пір, поки не буде досягнуто кінця списку. 
# Потім слова знову беруться з початкового списку.

# For example if 

# list = ['book', 'apple', 'word']
# books = randomWord(list)
# then possible output example 
# first call of next(books) returns apple
# second call of next(books) returns book
# third call of next(books) returns word
# fourth call of next(books) returns book

import random

def randomWord(list1):
    new_list1 = list1
    random.shuffle(new_list1)
    
    for item in range(len(new_list1)):
        yield new_list1[item]
        
    new_list2 = list1
    random.shuffle(new_list2)
    
    for item in range(len(new_list2)):
        yield new_list2[item]
    
    while True:
        yield None


list = ['book', 'apple', 'word']
books = randomWord(list)


print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))

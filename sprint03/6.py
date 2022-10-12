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

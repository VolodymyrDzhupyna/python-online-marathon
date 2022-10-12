# Створити функцію create з одним рядковим аргументом. 
# Ця функція повинна повертати анонімну функцію, яка перевіряє, 
# чи дорівнює аргумент функції аргументу зовнішньої функції. 

# For example: 

#  tom = create("pass_for_Tom") 

#  tom("pass_for_Tom") returns true 

#  tom("pass_for_tom") returns false

def create(words):
    return lambda x: x == words
    

print(create("pass_for_tom"))

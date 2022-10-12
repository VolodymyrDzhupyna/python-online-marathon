# Створити декоратор logger. Декоратор повинен виводити на консоль інформацію
# про ім'я функції та всі її аргументи, відокремлені символом ',' для функції, задекорованої logger.

# Створити функцію concat з довільною кількістю довільних аргументів, яка об'єднує аргументи, 
# та застосувати для цієї функції декоратор logger.

# For example

# print(concat(2, 3)) display
# Executing of function concat with arguments 2, 3...
# 23

# print(concat('hello', 2)) display
# Executing of function concat with arguments hello, 2...
# hello2

# print(concat (first = 'one', second = 'two')) display
# Executing of function concat with arguments one, two...
# onetwo

# Вкінці три крапки пропустили
# Executing of function concat with arguments 0, second kwarg...
# {тут вивід функції, яка обгортається} 
# Приклад з тесту.

def logger(func): # виводить в консоль інформацію
    def inner(*args, **kwargs):
        result = func(*args, **kwargs) # змінна на функцію concat
        args_generator = ", ".join(list((str(item) for item in args)))
        kwargs_generator = ", ".join(list(str(item) for item in kwargs.values()))
        value_args_kwargs = ", ".join(list((str(item) for item in args))
                            + list(str(item) for item in kwargs.values()))
        if args and kwargs:
            print((f"Executing of function {func.__name__} with arguments {value_args_kwargs}..."))
        elif args:
            print((f"Executing of function {func.__name__} with arguments {args_generator}..."))
        elif kwargs:
            print((f"Executing of function {func.__name__} with arguments {kwargs_generator}..."))
        return result
    return inner


@logger
def concat(*args, **kwargs):
    args_generator = list((str(item) for item in args))
    kwargs_generator = list(str(item) for item in kwargs.values())
    if args and kwargs:
        return "".join(args_generator + kwargs_generator)
    if args:
        return "".join(args_generator)
    if kwargs:
        return "".join(kwargs_generator)

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)


print(concat("first string", second = 2, third = "second string"))

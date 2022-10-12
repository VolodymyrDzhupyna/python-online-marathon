def logger(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
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

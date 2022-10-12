def outer(name):
    def inner():
        print(f"Hello, {name}!")
    return inner


tom = outer("Tom")
tom()
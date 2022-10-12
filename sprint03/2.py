def create(words):
    return lambda x: x == words
    

print(create("pass_for_tom"))

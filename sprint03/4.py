# Створити функцію-генератор дільників, яка повинна повертати всі дільники додатного числа.
# Якщо дільників не залишилось, функція повинна повернути None.

# three = divisor(3)
# next(three) => 1
# next(three) => 3
# next(three) => None

# num = 27
# for item in range(1, num+1):
#     if n % item == 0:
#         print(item)

def divisor(num):
    for item in range(1, num+1):
        if num % item == 0:
            yield item
    while True:
        yield None


three = divisor(3)
print(next(three))
print(next(three))
print(next(three))
print(next(three))

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

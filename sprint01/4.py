def findPermutation(p, q):

    r = []
    for item in q:
        if item in p:
            r.append(p.index(item) + 1)
    return r


p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]
print(findPermutation(p, q))

def cube(n):
    if n > 0:
        for i in range(n, 0, -1):
            yield i ** 3


def fib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_generator(n):
    for i in range(0, n):
        yield fib(i)

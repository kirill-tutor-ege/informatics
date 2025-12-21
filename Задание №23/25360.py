def f(n, finish):
    if n == finish:
        return 1
    if n < finish or n == 36:
        return 0
    return f(n - 3, finish) + f(n - 6, finish) + f(n // 2, finish)

print(f(86, 53) * f(53, 12))

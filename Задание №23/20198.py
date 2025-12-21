# Вариант 1
def f(n, finish, countA):
    if n == finish:
        return 1
    if n - 2 > finish:
        return 0
    
    if countA == 2:
        return f(n + 5, finish, 0) + f(n * 2, finish, 0)
    else:
        return f(n - 1, finish, countA + 1) + f(n + 5, finish, 0) + f(n * 2, finish, 0)

print(f(5, 34, 0))

# Вариант 2
def f(n, finish, cmdns):
    if n - 2 > finish or "AAA" in cmdns:
        return 0
    if n == finish:
        return 1
    return f(n - 1, finish, cmdns + "A") + f(n + 5, finish, cmdns + "B") + f(n * 2, finish, cmdns + "C")

print(f(5, 34, ""))

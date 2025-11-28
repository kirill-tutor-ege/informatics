def move(n):
    return n - 3, n - 5, n // 4

def end(n):
    return n <= 30

def win1(n):
    return any(end(x) for x in move(n)) and not end(n)

def lose1(n):
    return all(win1(x) for x in move(n))

def win2(n):
    return any(lose1(x) for x in move(n)) and not win1(n)

def lose12(n):
    return all(win1(x) or win2(x) for x in move(n)) and not lose1(n)

print("19: ", *[S for S in range(31, 10_000) if lose1(S)])
print("20: ", *[S for S in range(31, 10_000) if win2(S)])
print("21: ", *[S for S in range(31, 10_000) if lose12(S)])

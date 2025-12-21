def decToAny(n, base):
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return result[::-1]

for x in range(1, 27000 + 1):
    n = 3*27**9 +2*27**6 + 27**3 - x
    n = decToAny(n, 27)
    if n.count(0) == 6:
        print(x)
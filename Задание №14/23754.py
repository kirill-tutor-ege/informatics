def decToAny(n, base):
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return result[::-1]

for x in range(1, 3000 + 1):
    exp = decToAny(9*11**210 + 8*11**150 - x, 11)
    if exp.count(0) == 60:
        print(x)
def decToAny(n, base):
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return result[::-1]

exp = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
exp = decToAny(exp, 27)

# Вариант 1
count = exp.count(10) + exp.count(11) + ... + exp.count(26)

# Вариант 2
count = 0
for digit in exp:
    if digit > 9:
        count += 1

# Вариант 3
count = len([x for x in exp if x > 9])

print(count)

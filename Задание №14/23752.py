def decToAny(n, base):
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return result[::-1]

n = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
n = decToAny(n, 27)
count = 0
for x in n:
    if x > 9:
        count += 1
print(count)
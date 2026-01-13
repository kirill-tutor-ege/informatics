def two_digit(x):
    return 10 <= abs(x) <= 99

numbers = [int(x) for x in open("./files/23757.txt")]

min_00 = float('inf')
for x in numbers:
    if two_digit(x):
        min_00 = min(min_00, x)

count = 0
max_sum = -float('inf')
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if (two_digit(a) + two_digit(b) == 1) and ((a + b) % min_00 == 0):
        count += 1
        max_sum = max(max_sum, a + b)
print(count, max_sum)

numbers = [int(x) for x in open("./files/23563.txt")]

# Вариант 1
min_krat35 = float('inf')
for x in numbers:
    if (x > 0) and (x % 35 == 0):
        min_krat35 = min(min_krat35, x)

# Вариант 2
# min_krat35 = min(x for x in numbers if (x > 0) and (x % 35 == 0))

count = 0
max_sum = -float('inf')
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if (a != b) and (abs(a - b) % min_krat35 == 0):
        count += 1
        max_sum = max(max_sum, a + b)

print(count, max_sum)

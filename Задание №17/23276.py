def is_four(n):
    return 1000 <= abs(n) <= 9999

numbers = [int(x) for x in open("17_23276.txt")]

max_25 = max(x for x in numbers if abs(x) % 100 == 25)

count = 0
max_sum = 0
for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
    if (is_four(a) + is_four(b) + is_four(c) <= 2) and (a + b + c <= max_25):
        count += 1
        max_sum = max(max_sum, a + b + c)

print(count, max_sum)

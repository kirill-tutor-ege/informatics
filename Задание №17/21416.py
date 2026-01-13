numbers = [int(x) for x in open("./files/21416.txt")]

summ_negative = sum(x for x in numbers if x < 0)

count = 0
max_sum = -float('inf')
for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
    if max(a, b, c) * min(a, b, c) > summ_negative:
        count += 1
        max_sum = max(max_sum, a + b + c)
print(count, abs(max_sum))
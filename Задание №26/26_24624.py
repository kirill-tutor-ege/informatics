file = open("26_24624.txt")
N, K = [int(x) for x in file.readline().split()]

halls = []
for i in range(N):
    number, rows, cols = [int(x) for x in file.readline().split()]
    halls.append([[False] * cols for _ in range(rows)])

for i in range(K):
    hall, row, col = [int(x) for x in file.readline().split()]
    halls[hall - 1][row - 1][col - 1] = True

count = 0
min_row = float('inf')
for hall in halls:
    for row in range(len(hall)):
        if (row == len(hall) - 1) or (not any(hall[row + 1])):
            for seat in range(len(hall[row]) - 4):
                if not any(hall[row][seat:seat + 5]):
                    count += 1
                    min_row = min(min_row, row)

print(min_row + 1, count)

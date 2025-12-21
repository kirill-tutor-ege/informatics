line = open("24_25361.txt").readline()

max_len = 0
countF = 0
left = 0
right = 0
while right < len(line) - 1:
    if countF <= 76 and line[left] in "02468":
        right += 1
        if line[right] == 'F':
            countF += 1
        elif line[right] in "02468":
            left = right
            countF = 0
    else:
        if line[left] == 'F':
            countF -= 1
        left += 1

    if countF == 76:
        max_len = max(max_len, right - left + 1)

print(max_len)
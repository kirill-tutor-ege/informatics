line = open("24_16269.txt").readline()

max_len = 0
for i in range(len(line) - 1):
    if (line[i] == line[i + 1]) and (line[i] in "XYZ"):
        current_len = 2
        while   (i + current_len + 1 < len(line)) and (line[i + current_len] == line[i + current_len + 1]) and \
                (line[i + current_len] in "XYZ") and (line[i + current_len] != line[i + current_len - 1]):
            current_len += 2
        max_len = max(max_len, current_len)
print(max_len)

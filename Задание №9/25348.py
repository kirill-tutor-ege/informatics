lines = [[int(x) for x in line.split()] for line in open("files/25348.txt")]

count = 0
for line in lines:
    single = [x for x in line if line.count(x) == 1]
    triple = [x for x in line if line.count(x) == 3]
    if  (len(triple) == 3 and len(single) == 4) and \
        (max(line) not in triple):
        count += 1
print(count)

lines = [[int(y) for y in x.split()] for x in open("./files/24346.txt")]

answer = 0
number = 0
for line in lines:
    number += 1

    single = [x for x in line if line.count(x) == 1]
    repeated = [x for x in line if line.count(x) > 1]
    if  (len(single) > 0 and len(repeated) > 0) and\
        (sum(repeated)**2 > sum(single)**2) and\
        (sum(line) % 2 != 0):
        answer = number
print(answer)

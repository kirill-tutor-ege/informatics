def avg(list):
    return sum(list) / len(list)

lines = [[int(y) for y in x.split()] for x in open("./files/23747.txt")]

summa = 0
for line in lines:
    single = [x for x in line if line.count(x) == 1]
    repeated = [x for x in line if line.count(x) == 3]
    if  (len(single) == 4 and len(repeated) == 3) and\
        (avg(single) <= avg(repeated)):
        summa = sum(line)
print(summa)

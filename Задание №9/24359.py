lines = [[int(y) for y in x.split()] for x in open("./files/24359.txt")]

summa = 0
for line in lines:
    single = [x for x in line if line.count(x) == 1]
    double = [x for x in line if line.count(x) == 2]
    triple = [x for x in line if line.count(x) == 3]
    if  (len(triple) == 3 and len(double) == 2) and\
        ((sum(double) + sum(triple)) > sum(single)):
        summa = sum(line)
print(summa)

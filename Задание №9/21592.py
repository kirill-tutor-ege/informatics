lines = [[int(x) for x in line.split()] for line in open("./files/21592.txt")]

answer = 0
number = 0
for line in lines:
    number += 1

    single = [x for x in line if line.count(x) == 1]
    double = [x for x in line if line.count(x) == 2]
    if  (len(double) == 6 and len(single) == 2) and\
        (((max(double) - min(double))**2) > (sum(x**2 for x in single) * 2)):
        answer = number
print(answer)

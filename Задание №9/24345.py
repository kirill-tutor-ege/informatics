lines = [[int(y) for y in x.split()] for x in open("./files/24345.txt")]

for line in lines:
    line.sort()
    if  (line[-2]**2 > line[0] * line[-1]) and\
        (sum(line) % 2 == 0) and\
        (sum(x for x in line if x < 90) % 10 == 4):
        print(sum(line))
        break

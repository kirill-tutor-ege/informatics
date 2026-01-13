lines = [[int(y) for y in x.split()] for x in open("./files/24889.txt")]

count = 0
for line in lines:
    single = [x for x in line if line.count(x) == 1]
    triple = [x for x in line if line.count(x) == 3]
    fourth = [x for x in line if line.count(x) == 4]

    if  ((len(single) == 5 and max(line) in triple) or (len(single) == 4 and max(line) in fourth)) and\
        (max(single) + min(single) <= sum(single) - max(single) - min(single)):
        count += 1
print(count)


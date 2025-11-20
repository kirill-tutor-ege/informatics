file = open("26_23570.txt")

N, K = [int(x) for x in file.readline().split()]

lines = file.readlines()

all_dachas = [int(x) for x in lines[:N]]
snow_machines = [[int(y) for y in x.split()][::-1] for x in lines[N:]]
snow_machines.sort()

new = [snow_machines[0]]
for i in range(1, K):
    if new[-1][0] != snow_machines[i][0]:
        new.append(snow_machines[i])
    else:
        new[-1][1] = snow_machines[i][1]

total = 0
max_power = 0
for dacha in all_dachas:
    for x in new:
        if x[1] >= dacha:
            total += x[0]
            max_power = max(max_power, x[1])
            break
print(total, max_power)

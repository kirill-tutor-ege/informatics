file = open("26_25363.txt")

N = int(file.readline())
times = [[int(x) for x in line.split()] for line in file.readlines()]

sorted_list = []
for i in range(len(times)):
    sorted_list.append([times[i][0], i + 1, "Ожидание"])
    sorted_list.append([times[i][1], i + 1, "Активный"])
sorted_list.sort()

rating = ["Свободно"] * N
phones_ranged = [False] * N
last_phone_number = -1
for x in sorted_list:
    time, number, mode = x
    
    if not phones_ranged[number - 1]:
        if mode == "Ожидание":
            rating[rating.index("Свободно")] = number
        else:
            rating[-rating[::-1].index("Свободно") - 1] = number

        last_phone_number = number
        phones_ranged[number - 1] = True

print(last_phone_number, len(rating[rating.index(last_phone_number) + 1:]))

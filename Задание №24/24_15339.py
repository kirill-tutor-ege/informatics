line = open("24_15339.txt").readline().replace("B", "A").replace("C", "A").replace("7", "6").replace("8", "6").replace("9", "6")

while "AA" in line or "66" in line:
    line = line.replace("AA", "A A").replace("66", "6 6")

print(len(max(line.split(), key = len)))

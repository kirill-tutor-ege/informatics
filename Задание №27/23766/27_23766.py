def find_centroid(cluster):
    centroid = []
    min_distance = float('inf')

    for x0, y0 in cluster:
        sum_distance = 0
        for x, y in cluster:
            sum_distance += ((x0 - x)**2 + (y0 - y)**2) ** 0.5

        if sum_distance < min_distance:
            min_distance = sum_distance
            centroid = [x0, y0]

    return centroid

def find_max_distance(cluster, centroid):
    max_distance = -float('inf')

    x0, y0 = centroid
    for x, y in cluster:
        max_distance = max(max_distance, ((x0 - x)**2 + (y0 - y)**2) ** 0.5)

    return max_distance

points = [[float(y.replace(",", ".")) for y in x.split()] for x in open("27_B_23766.txt")]

cluster1 = []
cluster2 = []
cluster3 = []
for point in points:
    if 5 < point[0] < 30:
        if 17 < point[0] < 30:
            cluster1.append(point)
        elif point[0] > 0 and point[1] > 20:
            cluster2.append(point)
        elif point[0] > 0 and point[1] > 0:
            cluster3.append(point)

centroid1 = find_centroid(cluster1)
centroid2 = find_centroid(cluster2)
centroid3 = find_centroid(cluster3)

min_len = min(len(cluster1), len(cluster2), len(cluster3))
max_len = max(len(cluster1), len(cluster2), len(cluster3))

if len(cluster1) == min_len:
    min_centroid = centroid1
elif len(cluster2) == min_len:
    min_centroid = centroid2
elif len(cluster3) == min_len:
    min_centroid = centroid3

if len(cluster1) == max_len:
    max_centroid = centroid1
elif len(cluster2) == max_len:
    max_centroid = centroid2
elif len(cluster3) == max_len:
    max_centroid = centroid3

Q1 = ((max_centroid[0] - min_centroid[0])**2 + (max_centroid[1] - min_centroid[1])**2) ** 0.5
Q2 = max(find_max_distance(cluster1, centroid1), find_max_distance(cluster2, centroid2), find_max_distance(cluster3, centroid3))

print(abs(int(Q1 * 10000)), abs(int(Q2 * 10000)))

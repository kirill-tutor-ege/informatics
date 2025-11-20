find_centroid = lambda cluster: min((sum(((x0 - x)**2 + (y0 - y)**2) ** 0.5 for x, y in cluster), (x0, y0)) for x0, y0 in cluster)[1]

points = [[float(y) for y in x.split()] for x in open("27_17882_B.txt")]

cluster1 = []
cluster2 = []
cluster3 = []
for point in points:
    if point[1] > 7:
        cluster1.append(point)
    elif point[1] > 4:
        cluster2.append(point)
    else:
        cluster3.append(point)

print(1)
centroid1 = find_centroid(cluster1)
print(2)
centroid2 = find_centroid(cluster2)
print(3)
centroid3 = find_centroid(cluster3)

Px = (centroid1[0] + centroid2[0] + centroid3[0]) / 3
Py = (centroid1[1] + centroid2[1] + centroid3[1]) / 3

print(int(Px * 10000), int(Py * 10000))

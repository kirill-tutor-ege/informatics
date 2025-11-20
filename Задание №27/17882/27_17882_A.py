find_centroid = lambda cluster: min((sum(((x0 - x)**2 + (y0 - y)**2) ** 0.5 for x, y in cluster), (x0, y0)) for x0, y0 in cluster)[1]

points = [[float(y) for y in x.split()] for x in open("27_17882_A.txt")]

cluster1 = []
cluster2 = []
for point in points:
    if point[0] < 1:
        cluster1.append(point)
    else:
        cluster2.append(point)

centroid1 = find_centroid(cluster1)
centroid2 = find_centroid(cluster2)

Px = (centroid1[0] + centroid2[0]) / 2
Py = (centroid1[1] + centroid2[1]) / 2

print(int(Px * 10000), int(Py * 10000))

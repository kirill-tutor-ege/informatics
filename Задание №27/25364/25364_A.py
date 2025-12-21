from math import *

find_centroid = lambda cluster: min((sum(dist([x, y], [x0, y0]) for x, y in cluster), (x0, y0)) for x0, y0 in cluster)[1]

points = [[float(y.replace(",", ".")) for y in x.split()] for x in open("27_A_25364.txt")]

cluster1 = []
cluster2 = []
for point in points:
    if point[1] > 10:
        cluster1.append(point)
    else:
        cluster2.append(point)

centroid1 = find_centroid(cluster1)
centroid2 = find_centroid(cluster2)

P1 = min(dist([1, 1], centroid1), dist([1, 1], centroid2))
P2 = max(dist([1, 1], centroid1), dist([1, 1], centroid2))

print(int(P1 * 10000), int(P2 * 10000))

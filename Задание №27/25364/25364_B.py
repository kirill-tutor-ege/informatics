from math import *

count_points = lambda cluster, centroid, value : len([point for point in cluster if dist(point, centroid) <= value])
find_centroid = lambda cluster: min((sum(dist([x, y], [x0, y0]) for x, y in cluster), (x0, y0)) for x0, y0 in cluster)[1]

points = [[float(y.replace(",", ".")) for y in x.split()] for x in open("27_B_25364.txt")]

cluster1 = []
cluster2 = []
cluster3 = []
for point in points:
    if point[1] > 23:
        cluster1.append(point)
    elif point[1] > 15:
        cluster2.append(point)
    else:
        cluster3.append(point)

if max(len(cluster1), len(cluster2), len(cluster3)) == len(cluster1):
    max_cluster = cluster1
elif max(len(cluster1), len(cluster2), len(cluster3)) == len(cluster2):
    max_cluster = cluster2
else:
    max_cluster = cluster3

centroid = find_centroid(max_cluster)

Q1 = count_points(max_cluster, centroid, 1.2)
Q2 = count_points(max_cluster, centroid, 0.75)

print(Q1, Q2)

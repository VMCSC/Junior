start = 3
end = 6
v = 9

edges = [
    (0, 2, 5),
    (0, 5, 2),
    (1, 2, 4),
    (1, 4, 6),
    (1, 5, 3),
    (2, 6, 8),
    (2, 7, 11),
    (3, 4, 9),
    (3, 5, 1),
    (3, 8, 5),
    (4, 7, 3),
    (7, 8, 1)
]

dist = [10000 for i in range(v)]
dist[start] = 0

for i in range(v-1):
    for j in edges:
        startingVertex = j[0]
        endingVertex = j[1]
        weight = j[2]
        if dist[startingVertex] + weight < dist[endingVertex]:
            dist[endingVertex] = dist[startingVertex] + weight
        if dist[endingVertex] + weight < dist[startingVertex]:
            dist[startingVertex] = dist[endingVertex] + weight

print(dist[end])
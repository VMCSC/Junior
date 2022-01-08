import pprint

v = 9
adjacencyMatrix = [[10000000 for i in range(v)] for j in range(v)]

for i in range(v):
    adjacencyMatrix[i][i] = 0

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

for edge in edges:
    adjacencyMatrix[edge[0]][edge[1]] = edge[2]
    adjacencyMatrix[edge[1]][edge[0]] = edge[2]

for b in range(v):
    for a in range(v):
        for c in range(v):
            if adjacencyMatrix[a][b] + adjacencyMatrix[b][c] < adjacencyMatrix[a][c]:
                adjacencyMatrix[a][c] = adjacencyMatrix[a][b] + adjacencyMatrix[b][c]

pprint.pprint(adjacencyMatrix)
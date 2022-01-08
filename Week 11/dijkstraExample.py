import queue

start = 8
end = 1
v = 9

graph = [
    [(5, 2), (2, 5)],
    [(2, 4), (4, 6), (5, 3)],
    [(0, 5), (1, 4), (6, 8), (7, 11)],
    [(4, 9), (5, 1), (8, 5)],
    [(1, 6), (3, 9), (7, 3)],
    [(0, 2), (1, 3), (3, 1)],
    [(2, 8)],
    [(2, 11), (4, 3), (8, 1)],
    [(3, 5), (7, 1)]
]

dist = [10000 for i in range(v)]
dist[start] = 0

pQ = queue.PriorityQueue()
pQ.put((0, start))

while not pQ.empty():
    cur = pQ.get()
    totalWeight = cur[0]
    node = cur[1]
    for adjacentVertex in graph[node]:
        newTotalWeight = totalWeight + adjacentVertex[1]
        nextNode = adjacentVertex[0]
        if dist[nextNode] > newTotalWeight:
            dist[nextNode] = newTotalWeight
            pQ.put((newTotalWeight, nextNode))

print(dist[end])
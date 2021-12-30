import queue
n, m, a, b = [int(i) for i in input().split()]
adjacencyList = [[] for i in range(n+1)]

visited=[False for i in range(n+1)]

q = queue.Queue()
q.put(a)

visited[a] = True

for i in range(m):
    x, y = [int(i) for i in input().split()]
    adjacencyList[x].append(y)
    adjacencyList[y].append(x)

while not q.empty():
    c = q.get()
    if c == b:
        print("GO SHAHIR!")
        break
    for adjacentNodes in adjacencyList[c]:
        if not visited[adjacentNodes]:
            visited[adjacentNodes] = True
            q.put(adjacentNodes)

if not visited[b]:
    print("NO SHAHIR!")

n, m, a, b = [int(i) for i in input().split()]
adjacencyList = [[] for i in range(n+1)]

visited=[False for i in range(n+1)]

visited[a] = True

for i in range(m):
    x, y = [int(i) for i in input().split()]
    adjacencyList[x].append(y)
    adjacencyList[y].append(x)

def dfs(node):
    for adjacentNodes in adjacencyList[node]:
        if not visited[adjacentNodes]:
            visited[adjacentNodes] = True
            dfs(adjacentNodes)

dfs(a)

if not visited[b]:
    print("NO SHAHIR!")
else:
    print("GO SHAHIR!")
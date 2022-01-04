import queue
n, t = [int(i) for i in input().split()]
adjacencyList = {'home' : [], 'Waterloo GO' : []}
visited = {'home' : True, 'Waterloo GO' : False}
for i in range(n):
    station = input()
    adjacencyList[station] = []
    visited[station] = False

for i in range(t):
    a, b = input().split("-")
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)

q = queue.Queue()
q.put(('home', 0))

while not q.empty():
    c = q.get()
    if c[0] == 'Waterloo GO':
        print(c[1])
        break
    for nodes in adjacencyList[c[0]]:
        if not visited[nodes]:
            visited[nodes] = True
            q.put((nodes, c[1] + 1))

if not visited['Waterloo GO']:
    print('RIP ACE')
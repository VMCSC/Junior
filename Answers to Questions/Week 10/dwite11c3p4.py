import queue

for testCases in range(5):
    r, c = [int(i) for i in input().split()]
    maze = [input() for i in range(r)]
    aPos = (-1, -1)
    bPos = (-1, -1)
    cPos = (-1, -1)
    for x in range(r):
        if maze[x].find("A") != -1:
            aPos = (x, maze[x].find("A"))
        if maze[x].find("B") != -1:
            bPos = (x, maze[x].find("B"))
        if maze[x].find("C") != -1:
            cPos = (x, maze[x].find("C"))
    
    abCost = -1
    bcCost = -1
    acCost = -1

    visited = [[False for j in range(c)] for i in range(r)]

    visited[aPos[0]][aPos[1]] = True

    q = queue.Queue()
    
    q.put((aPos, 0))

    while not q.empty():
        firstQueue = q.get()
        current = firstQueue[0]
        distance = firstQueue[1]
        if visited[bPos[0]][bPos[1]] and visited[cPos[0]][cPos[1]]:
            break
        
        if current[0] != 0 and maze[current[0] - 1][current[1]] != "#":
            if maze[current[0]-1][current[1]] == "B" and not visited[bPos[0]][bPos[1]]:
                abCost = distance + 1
            if maze[current[0]-1][current[1]] == "C" and not visited[cPos[0]][cPos[1]]:
                acCost = distance + 1
            visited[current[0]-1][current[1]] = True
            q.put(((current[0] - 1, current[1]), distance + 1))
        if current[1] != 0 and maze[current[0]][current[1] - 1] != "#":
            if maze[current[0]][current[1] - 1] == "B" and not visited[bPos[0]][bPos[1]]:
                abCost = distance + 1
            if maze[current[0]][current[1] - 1] == "C" and not visited[cPos[0]][cPos[1]]:
                acCost = distance + 1
            visited[current[0]][current[1] - 1] = True
            q.put(((current[0], current[1] - 1), distance + 1))
        if current[0] + 1 != r and maze[current[0] + 1][current[1]] != "#":
            if maze[current[0]+1][current[1]] == "B" and not visited[bPos[0]][bPos[1]]:
                abCost = distance + 1
            if maze[current[0]+1][current[1]] == "C" and not visited[cPos[0]][cPos[1]]:
                acCost = distance + 1
            visited[current[0]+1][current[1]] = True
            q.put(((current[0] + 1, current[1]), distance + 1))
        if current[1] + 1 != c and maze[current[0]][current[1] + 1] != "#":
            if maze[current[0]][current[1] + 1] == "B" and not visited[bPos[0]][bPos[1]]:
                abCost = distance + 1
            if maze[current[0]][current[1] + 1] == "C" and not visited[cPos[0]][cPos[1]]:
                acCost = distance + 1
            visited[current[0]][current[1] + 1] = True
            q.put(((current[0], current[1] + 1), distance + 1))

    visited = [[False for j in range(c)] for i in range(r)]

    visited[aPos[0]][aPos[1]] = True

    q = queue.Queue()
    
    q.put((bPos, 0))

    while not q.empty():
        firstQueue = q.get()
        current = firstQueue[0]
        distance = firstQueue[1]
        if visited[cPos[0]][cPos[1]]:
            break
        
        if current[0] != 0 and maze[current[0] - 1][current[1]] != "#":
            if maze[current[0]-1][current[1]] == "C" and not visited[cPos[0]][cPos[1]]:
                bcCost = distance + 1
            visited[current[0]-1][current[1]] = True
            q.put(((current[0] - 1, current[1]), distance + 1))
        if current[1] != 0 and maze[current[0]][current[1] - 1] != "#":
            if maze[current[0]][current[1] - 1] == "C" and not visited[cPos[0]][cPos[1]]:
                bcCost = distance + 1
            visited[current[0]][current[1] - 1] = True
            q.put(((current[0], current[1] - 1), distance + 1))
        if current[0] + 1 != r and maze[current[0] + 1][current[1]] != "#":
            if maze[current[0]+1][current[1]] == "C" and not visited[cPos[0]][cPos[1]]:
                bcCost = distance + 1
            visited[current[0]+1][current[1]] = True
            q.put(((current[0] + 1, current[1]), distance + 1))
        if current[1] + 1 != c and maze[current[0]][current[1] + 1] != "#":
            if maze[current[0]][current[1] + 1] == "C" and not visited[cPos[0]][cPos[1]]:
                bcCost = distance + 1
            visited[current[0]][current[1] + 1] = True
            q.put(((current[0], current[1] + 1), distance + 1))
    
    print(abCost + acCost + bcCost)
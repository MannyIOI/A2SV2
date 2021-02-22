def bfs(n, m, edges, s):
    graph = {}
    distance = {}
    for i in range(n):
        if i + 1 != s:
            distance[i + 1] = -1
        
    for i in range(len(edges)):
        edge = edges[i]

        if edge[0] not in graph:
            graph[edge[0]] = [edge[1]]
        else:
            graph[edge[0]].append(edge[1])
    
    queue = [s]
    while len(queue) > 0:
        item = queue.pop(0)
        if item in graph:
            for i in graph[item]:
                queue.append(i)
                if item == s:
                    distance[i] = 6
                else:
                    if distance[i] > 0:
                        distance[i] = min(distance[item] + 6, distance[i])
                    else:
                        distance[i] = distance[item] + 6
                
    return distance.values()

# print(bfs(4, 2, [[1, 2], [1, 3]], 1))
print(bfs(5, 3, [[1, 2], [1, 3], [3, 4], [2, 5], [5, 4]], 1))
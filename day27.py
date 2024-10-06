from collections import deque

def shortest_path(V,edges,start,end):
    #create adjacency list
    adj_list=[[] for _ in range(V)]
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    queue =deque([(start,[start])])
    visited=set([start])

    while queue:
        node,path=queue.popleft()

        if node == end:
            return path
        for neighbour in adj_list[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,path+[neighbour]))
    return None
V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start = 0
end = 4


shortest_path_result = shortest_path(V, edges, start, end)
print("Shortest Path:", shortest_path_result) #Shortest Path: [0, 1, 3, 4]


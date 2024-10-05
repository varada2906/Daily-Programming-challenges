def cycle(V,edges):
    from collections import defaultdict
#defaultdict is used to give the adjacency list from the given graph
    #Build the adjacency list 
    adj_list=defaultdict(list)
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    #to track the visited nodes
    visited =[False]*V

    #dfs function to check for cycles
    def dfs(v,parent):
        visited[v]=True
        for neighbour in adj_list[v]:
            if not visited[neighbour]:
                if dfs(neighbour,v):
                    return True
            elif neighbour != parent:
                return True
        return False
    
    for i in range(V):
        if not visited[i]:
            if dfs(i,-1):
                return True
    return False

V = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
print(cycle(V, edges))  # Output: True


"""Adjacency list:we first build an adjancency list from the edges provided
Visited Array:We maintain a visited array to mark the nodes that have been explored
,dfs is used :for each unvisited node,we perform a dfs .During dfs,if we encounter an already visited node 
that is not a parent node ,a cycle is detected .It will return true if there is cycle in the graph"""


    
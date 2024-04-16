def dfs(graph, vertex, visited, spanning_tree):
    visited[vertex] = True
    for v in range(len(graph[vertex])):
        if graph[vertex][v] == 1 and not visited[v]:
            spanning_tree[vertex][v] = 1  
            spanning_tree[v][vertex] = 1  
            dfs(graph, v, visited, spanning_tree)

def spanning_tree_dfs(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n  
    spanning_tree = [[0] * n for _ in range(n)] 

    dfs(adj_matrix, 0, visited, spanning_tree)

    return spanning_tree

adj_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

spanning_tree = spanning_tree_dfs(adj_matrix)
for row in spanning_tree:
    print(row)
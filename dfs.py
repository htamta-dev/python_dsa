def dfs(graph, node, visited):
    # Depth First Search (DFS) implementation
    if node not in visited:
        print(f"{ "->" if len(visited) else ""} {node}", end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def test_dfs():
    # Test cases for DFS
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    visited = set()
    print("DFS Traversal of the graph:")
    dfs(graph, 'A', visited)
    print()
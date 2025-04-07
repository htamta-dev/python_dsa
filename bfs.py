from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

def test_bfs():

    graph = {
        'A': ['B', 'C'],
        'B': ['A','D', 'E'],
        'C': ['A','F'],
        'D': ['B'],
        'E': ['B','F'],
        'F': ['C','E']
    }

    start_node = 'A'
    print("BFS Traversal of the graph:")
    bfs_result = bfs(graph, start_node)
    print(" -> ".join(bfs_result))
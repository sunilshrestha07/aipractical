visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        # Print the node
        print(node, end="->" if any(neighbor not in visited for neighbor in graph[node]) else " ")
        visited.add(node)  # Mark the node as visited
        for neighbour in graph[node]:  # Explore neighbors
            dfs(visited, graph, neighbour)

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print("Following is the Depth-First Search:")
dfs(visited, graph, '5')

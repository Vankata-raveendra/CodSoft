def iddfs(graph, start, goal, max_depth):
    for depth_limit in range(max_depth + 1):
        result = dls(graph, start, goal, depth_limit)
        if result is not None:
            return result
    return None

def dls(graph, start, goal, depth_limit):
    visited = set()
    return dls_recursive(graph, start, goal, depth_limit, visited)

def dls_recursive(graph, current_node, goal, depth_limit, visited, depth=0):
    if depth > depth_limit:
        return None  # Depth limit reached, backtrack

    print(current_node, end=' ')

    if current_node == goal:
        return [current_node]  # Goal node found

    visited.add(current_node)

    if depth == depth_limit:
        return None  # Reached depth limit, backtrack

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            result = dls_recursive(graph, neighbor, goal, depth_limit, visited, depth + 1)
            if result is not None:
                result.insert(0, current_node)  # Prepend current node to the result
                return result  # Goal found in deeper level, return the path
    
    return None  # Goal not found at this level

# Input the number of vertices
vertex = int(input("Enter the number of vertices: "))

# Initialize the graph
graph = {}
for _ in range(vertex):
    node = input("Enter the node: ")
    graph[node] = []

# Input the number of edges
edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    node1, node2 = input("Enter the nodes (space-separated): ").split()
    graph[node1].append(node2)
    graph[node2].append(node1)

# Input the starting node and the goal node for IDDFS
start_node = input("Enter the starting node for IDDFS: ")
goal_node = input("Enter the goal node for IDDFS: ")
max_depth = int(input("Enter the maximum depth for IDDFS: "))

# Perform IDDFS
print("IDDFS traversal:")
result = iddfs(graph, start_node, goal_node, max_depth)
if result:
    print(f"\nGoal node {goal_node} found within depth limit. Path: {' -> '.join(result)}")
else:
    print(f"\nGoal node {goal_node} not found within depth limit.")

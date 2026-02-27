# Constraint Satisfaction Problem - Map Coloring

# Define the map (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store final assignment
solution = {}

# Check if assigning color is valid
def is_valid(node, color):
    for neighbor in graph[node]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

# Backtracking function
def backtrack():
    # If all nodes are assigned, return True
    if len(solution) == len(graph):
        return True

    # Select unassigned node
    for node in graph:
        if node not in solution:
            break

    # Try all colors
    for color in colors:
        if is_valid(node, color):
            solution[node] = color
            if backtrack():
                return True
            # Backtrack
            del solution[node]

    return False


# Run CSP solver
if backtrack():
    print("Solution Found:")
    for node in solution:
        print(node, "->", solution[node])
else:
    print("No solution exists.")
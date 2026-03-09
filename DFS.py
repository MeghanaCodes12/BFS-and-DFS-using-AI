def DFS(graph, start, dest):
    stack = []
    visited = []

    stack.append(start)
    result = ["Not reachable", []]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            if node == dest:
                print("Destination node found:", node)
                result[0] = "Reachable"
                break

            print(node, "is not the destination node")

            for child in reversed(graph[node]):  
                if child not in visited:
                    stack.append(child)

    result[1] = visited
    return result


# -------- Graph Input --------

n = int(input("Enter number of nodes: "))

nodes = []
graph = {}

print("\nEnter node names:")
for i in range(n):
    node = input(f"Enter node {i+1}: ")
    nodes.append(node)

print("\nEnter neighbours for each node (space separated):")
for node in nodes:
    neighbors = input(f"Neighbours of {node}: ").split()
    graph[node] = neighbors


# -------- DFS Inputs --------

start = input("\nEnter start node: ")
dest = input("Enter destination node: ")

result = DFS(graph, start, dest)

print("\nResult:", result[0])
print("Traversal path:", result[1])
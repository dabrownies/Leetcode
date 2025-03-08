queue = [1]

adj = []

# traverse through the graph 
def copy(root):
    for edge in adj:
        node = edge[0]
        node.neighbors.append(edge[1])
    return root








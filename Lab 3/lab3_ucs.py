wgraph = {
    "A": [("B", 1), ("C", 10)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 2), ("G", 2)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}
 
visited = []
pqueue = []
 
def ucs(node):
    pqueue.append((0, node, [node]))
    while pqueue:
        pqueue.sort()
        print(pqueue, visited)
        cost, temp, path = pqueue.pop(0)
        if temp not in visited:
            visited.append(temp)
            if temp == "G":
                print("Goal found! Path:", path, "Total cost:", cost)
                return path, cost
            for child, weight in wgraph[temp]:
                pqueue.append((cost + weight, child, path + [child]))
 
ucs("A")
print("pqueue, visited")

"""Lab 4: Informed Search - A* (sir ke pattern mein).
Campus graph: S -> G with heuristic.
Run: python lab4.py
"""

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

h_zero = {"S": 0, "A": 0, "B": 0, "C": 0, "G": 0}

h_over = {"S": 5, "A": 4, "B": 4, "C": 10, "G": 0}

visited = []
pqueue = []


def astar(node, heuristic):
    pqueue.append((0 + heuristic[node], 0, node, [node]))
    while pqueue:
        pqueue.sort()
        print(pqueue, visited)
        f, cost, temp, path = pqueue.pop(0)
        if temp not in visited:
            visited.append(temp)
            if temp == "G":
                print("Goal found! Path:", path, "Total cost:", cost)
                return path, cost
            for child, weight in graph[temp]:
                g_new = cost + weight
                f_new = g_new + heuristic[child]
                pqueue.append((f_new, g_new, child, path + [child]))


print("===== Task 2a: A* with supplied heuristic =====")
visited = []
pqueue = []
astar("S", h)
print("pqueue, visited")

print()
print("===== Task 2b: UCS (zero heuristic) =====")
visited = []
pqueue = []
astar("S", h_zero)
print("pqueue, visited")

print()
print("===== Task 3: A* with overestimate h(C)=10 =====")
visited = []
pqueue = []
astar("S", h_over)
print("pqueue, visited")

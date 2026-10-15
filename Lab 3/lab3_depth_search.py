graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
 
visited = []
stack = []
 
def dls(node, limit):
    stack.append((node, 0, [node]))
    cutoff = False
    while stack:
        print(stack, visited)
        temp, depth, path = stack.pop()
        if temp not in visited:
            visited.append(temp)
            if temp == "G":
                print("Goal found:", temp, "Path:", path)
                return "FOUND", path
            if depth < limit:
                for child in graph[temp]:
                    stack.append((child, depth + 1, path + [child]))
            elif graph[temp]:
                cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None
 
def iddfs(node, max_limit):
    global visited, stack
    for limit in range(1, max_limit + 1):
        visited = []
        stack = []
        print("--- Limit:", limit, "---")
        result, path = dls(node, limit)
        print("Limit", limit, "Result:", result, "Path:", path)
        if result == "FOUND":
            break
 
iddfs("A", 4)
print("stack, visited")

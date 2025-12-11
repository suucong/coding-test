n = int(input())
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dist = [-1] * (n + 1)

def dfs(current, relation_count):
    dist[current] = relation_count

    if current == b:
        return

    for neighbor in graph[current]:
        if dist[neighbor] == -1:
            dfs(neighbor, relation_count + 1)

dist[a] = 0 
dfs(a, 0)
print(dist[b])
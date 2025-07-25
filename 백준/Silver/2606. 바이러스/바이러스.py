N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    count = 0

    for i in G[v]:
        if not visited[i]:
            count += 1 + dfs(i)
    return count

print(dfs(1))

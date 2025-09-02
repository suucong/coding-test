import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dfs(node, dist):
    visited[node] = True
    far_node, max_dist = node, dist

    for nxt, weight in graph[node]:
        if not visited[nxt]:
            n_node, n_dist = dfs(nxt, dist + weight)
            if n_dist > max_dist:
                far_node, max_dist = n_node, n_dist

    return far_node, max_dist

visited = [False] * (n+1)
node, _ = dfs(1, 0)

visited = [False] * (n+1)
_, diameter = dfs(node, 0)

print(diameter)

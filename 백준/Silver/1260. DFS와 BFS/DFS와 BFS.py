from collections import deque

N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    # 양방향 그래프 처리
    G[u].append(v)
    G[v].append(u)

for i in range(N + 1):
    G[i].sort()

def DFS(V, visited = [0] * (N + 1)):
    visited[V] = 1
    print(V, end=" ")

    for i in G[V]:
        if visited[i] == 0:
            DFS(i, visited)

def BFS(V):
    queue = deque([V])
    visited = [0] * (N + 1)
    visited[V] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in G[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

DFS(V)
print()
BFS(V)
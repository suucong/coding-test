from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, graph, color):
    q = deque([start])
    color[start] = 1

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if color[nxt] == 0:
                color[nxt] = -color[v]
                q.append(nxt)
            elif color[nxt] == color[v]:
                return False
    return True

def is_bipartite(v, graph):
    color = [0] * (v + 1)
    for i in range(1, v+1):
        if color[i] == 0:
            if not bfs(i, graph, color):
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print("YES" if is_bipartite(v, graph) else "NO")
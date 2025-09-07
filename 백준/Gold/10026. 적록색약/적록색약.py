from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, graph):
    q = deque([(x, y)])
    visited[x][y] = True
    color = graph[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

# 적록색약이 아닌사람
visited = [[False] * n for _ in range(n)]
count_n = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited, graph)
            count_n += 1

# 적록색약인 사람
visited = [[False] * n for _ in range(n)]
count_rg = 0
for i in range(len(graph)):
    graph[i] = ['R' if x == 'G' else x for x in graph[i]]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited, graph)
            count_rg += 1

print(count_n, count_rg)



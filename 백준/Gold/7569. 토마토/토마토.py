from collections import deque
import sys
input = sys.stdin.readline

def bfs(m, n, h, graph):
    q = deque()

    # 익은 토마토 모두 큐에 삽입
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    q.append((x, y, z))

    dx_dy_dz = [(0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0)]

    while q:
        x, y, z = q.popleft()
        for dx, dy, dz in dx_dy_dz:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nx, ny, nz))

    # 모두 탐색이 끝난 후 날짜 계산
    days = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 0:
                    return -1
                days = max(days, graph[z][y][x])
    return days - 1

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
print(bfs(m, n, h, box))
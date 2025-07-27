from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
q = deque()
q.append((0, 0, 1))

while q:
    x, y, distance = q.popleft()

    if 0 <= x < M and 0 <= y < N:
        if graph[y][x] == 1:
            graph[y][x] = 0
            if x == M - 1 and y == N - 1:
                print(distance)
                break

            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            for i in range(4):
                q.append((x + dx[i], y + dy[i], distance + 1))

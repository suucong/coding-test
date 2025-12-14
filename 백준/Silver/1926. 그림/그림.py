from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
num_of_pic = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            num_of_pic += 1
            size = 0

            q = deque([(i, j)])
            graph[i][j] = 0

            while q:
                y, x = q.popleft()
                size += 1

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < m and 0 <= ny < n:
                        if graph[ny][nx] == 1:
                            graph[ny][nx] = 0
                            q.append((ny, nx))

            if size > max_size:
                max_size = size

print(num_of_pic)
print(max_size)
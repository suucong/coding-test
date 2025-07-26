import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

def dfs(x, y):
    count = 0
    if x < 0 or x >= N or y < 0 or y >= N:
        return count
    if graph[y][x] == 0:
        return count
    graph[y][x] = 0
    count += 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        count += dfs(x + dx[i], y + dy[i])
    return count

a = 0
b = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            b.append(dfs(x, y))
            a += 1
print(a)
b.sort()
for v in b:
    print(v)
import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]

def dfs(start, cur):
    for nxt in range(N):
        if G[cur][nxt] == 1 and not visited[nxt]:
            visited[nxt] = True
            result[start][nxt] = 1
            dfs(start, nxt)

for i in range(N):
    visited = [False] * N
    dfs(i, i)

for row in result:
    print(*row)
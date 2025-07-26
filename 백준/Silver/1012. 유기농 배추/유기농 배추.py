import sys  
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if G[y][x] == 0:
        return
    G[y][x] = 0

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        dfs(x + dx[i], y + dy[i])

T = int(input())
answers = []
for _ in range(T):
    M, N, K = map(int, input().split())
    G = [[0] * M for _ in range(N)]
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        G[y][x] = 1
    for y in range(N):
        for x in range(M):
            if G[y][x] == 1:
                dfs(x, y)
                count += 1
    answers.append(count)

for answer in answers:
    print(answer)
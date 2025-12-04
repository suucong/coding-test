N, M = map(int, input().split())
visited = [False] * (N + 1)

def backtrack(path, c):
    if len(path) == M:
        for v in path:
            print(v, end=' ')
        print()

    for i in range(c + 1, N + 1):
        if not visited[i]:
            visited[i] = True
            backtrack(path + [i], i)
            visited[i] = False

backtrack([], 0)
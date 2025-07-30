N, M = map(int, input().split())
used = [False] * (N + 1)

def backtrack(path):
    if len(path) == M:
        for v in path:
            print(v, end=' ')
        print()
        return
    for i in range(1, N + 1):
        if not used[i]:
            used[i] = True
            backtrack(path + [i])
            used[i] = False

backtrack([])
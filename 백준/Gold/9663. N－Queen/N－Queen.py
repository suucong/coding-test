N = int(input())
G = [0] * N
answer = 0

def is_validated(row):
    for pv_r in range(row):
        if (G[pv_r] == G[row] or
            abs(row - pv_r) == abs(G[row] - G[pv_r])):
            return False
    return True

def backtrack(row):
    global answer

    if row == N:
        answer += 1
        return

    for col in range(N):
        G[row] = col
        if is_validated(row):
            backtrack(row + 1)

backtrack(0)
print(answer)
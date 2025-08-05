T = int(input())
cases = [int(input()) for _ in range(T)]

m = max(cases)
dy = [0] * (m + 1)
dy[0] = 1
dy[1] = 1
dy[2] = 2

for i in range(3, m + 1):
    dy[i] = dy[i - 3] + dy[i - 2] + dy[i - 1]

for c in cases:
    print(dy[c])
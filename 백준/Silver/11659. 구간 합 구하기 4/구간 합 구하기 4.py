N, M = map(int, input().split())
a = list(map(int, input().split()))
b = [tuple(map(int, input().split())) for _ in range(M)]

S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i - 1] + a[i - 1]

for i, j in b:
    print(S[j] - S[i - 1])

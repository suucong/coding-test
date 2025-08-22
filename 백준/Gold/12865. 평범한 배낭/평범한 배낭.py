n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = items[i-1]
    for w in range(1, k+1):
        if w < weight:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

print(dp[n][k])
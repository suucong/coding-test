n = int(input())
scores = [int(input()) for _ in range(n)]

if n == 1:
    print(scores[0])
elif n == 2:
    print(scores[0] + scores[1])
else:
    dp = [0] * n

    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])

    print(dp[n - 1])
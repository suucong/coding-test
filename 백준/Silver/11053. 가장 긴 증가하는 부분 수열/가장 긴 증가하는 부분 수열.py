N = int(input())
A = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = 1
answer = 1

for i in range(2, N + 1):
    m = 0
    for j in range(i - 1, 0, -1):
        if A[j] < A[i] and dp[j] > m:
            m = dp[j]
    dp[i] = m + 1
    if dp[i] > answer:
        answer = dp[i]

print(answer)
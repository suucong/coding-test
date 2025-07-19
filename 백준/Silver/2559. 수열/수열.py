N, K = map(int, input().split())
temps = list(map(int, input().split()))
cnt = 0
for i in range(K):
    cnt += temps[i]
answer = cnt

for i in range(N - K):
    cnt = cnt - temps[i] + temps[K + i]
    if cnt > answer:
        answer = cnt

print(answer)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            cnt = cards[i] + cards[j] + cards[k]
            if cnt <= M and (M - cnt) < (M - answer):
                answer = cnt

print(answer)

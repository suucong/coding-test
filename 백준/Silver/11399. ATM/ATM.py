N = int(input())
P = list(map(int, input().split()))
P.sort()
answer = 0
cnt = 0
for p in P:
    cnt += p
    answer += cnt
print(answer)
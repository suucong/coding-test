N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)

cnt = 0
for a in A:
    cnt += K // a
    K %= a
print(cnt)
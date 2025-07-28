N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
b = [(b, idx) for idx, b in enumerate(B)]
b.sort()
a = [0] * N
for i in range(N):
    a[b[i][1]] = A[i]
A = a

answer = 0
for j in range(N):
    answer += A[j] * B[j]

print(answer)
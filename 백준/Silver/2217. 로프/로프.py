N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()
answer = 0

for i in range(N):
    if arr[i]*(N-i) > answer:
        answer = arr[i] * (N-i)

print(answer)
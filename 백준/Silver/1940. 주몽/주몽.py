N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
lt, rt = 0, len(arr) - 1
answer = 0

while lt < rt:
    cnt = arr[lt] + arr[rt]
    if cnt == M:
        answer += 1
        rt -= 1
    elif cnt < M:
        lt += 1
    else:
        rt -= 1

print(answer)



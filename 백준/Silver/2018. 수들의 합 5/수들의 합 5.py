N = int(input())
lt = 1
rt = 2
cnt = lt
answer = 0

while True:
    if cnt < N:
        if rt > N:
            break
        else:
            cnt += rt
            rt += 1
    elif cnt == N:
        answer += 1
        cnt -= lt
        lt += 1
    elif cnt > N:
        cnt -= lt
        lt += 1

print(answer)
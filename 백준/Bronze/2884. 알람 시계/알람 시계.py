time = list(map(int, input().split()))
changed_time = time

if time[1] < 45:
    changed_time[1] = 60 + time[1] - 45
    if time[0] > 0:
        changed_time[0] = time[0] - 1
    else:
        changed_time[0] = 23
else:
    changed_time[1] = time[1] - 45

# 결과 출력
print(" ".join(map(str, changed_time)))

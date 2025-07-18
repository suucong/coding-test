K = int(input())
stack = []
answer = 0

for _ in range(K):
    num = int(input())
    if num == 0 :
        if stack:
            m = stack.pop()
            answer -= m
    else:
        stack.append(num)
        answer += num

print(answer)

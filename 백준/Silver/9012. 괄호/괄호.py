def solution(str):
    answer = "NO"
    stack = []
    for c in str:
        if c == '(':
            stack.append(c)
        elif c == ')' and len(stack) > 0:
            stack.pop()
        elif c == ')' and len(stack) == 0:
            return answer

    if len(stack) == 0:
        answer = "YES"
    return answer

T = int(input())
arr = [input() for _ in range(T)]
for str in arr:
    print(solution(str))
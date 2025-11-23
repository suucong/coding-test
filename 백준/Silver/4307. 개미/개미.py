import sys
input = sys.stdin.readline

t = int(input())
answer = []
for _ in range(t):
    min_answer = 0
    max_answer = 0
    i, n = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    for v in arr:
        b = max(i - v, v)
        if min(i - v, v) > min_answer:
            min_answer = min(i - v, v)
        if max(i - v, v) > max_answer:
            max_answer = max(i - v, v)
    answer.append((min_answer, max_answer))

for a, b in answer:
    print(a, b)
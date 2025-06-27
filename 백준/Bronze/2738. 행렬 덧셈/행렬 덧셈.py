N, M = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]

for a, b in zip(A, B):
    for x, y in zip(a, b):
        print(x + y, end = ' ')
    print()
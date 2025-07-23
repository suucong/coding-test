N = int(input())
a = [tuple(map(int, input().split())) for _ in range(N)]

a.sort()
for x, y in a:
    print(f'{x} {y}')
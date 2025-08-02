L, C = map(int, input().split())
arr = input().split()
arr.sort()
visited = [False] * C

def backtrack(start, pw):
    if len(pw) == L:
        v = sum(1 for ch in pw if ch in 'aeiou')
        c = L - v
        if v >= 1 and c >= 2:
            print(pw)
        return

    for i in range(start, C):
        backtrack(i + 1, pw + arr[i])

backtrack(0, '')

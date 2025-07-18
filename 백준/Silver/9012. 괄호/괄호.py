n = int(input())
datas = []
for _ in range(n):
    datas.append(input())

def is_valid(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    if not stack:
        return True

for data in datas:
    if is_valid(data):
        print("YES")
    else:
        print("NO")

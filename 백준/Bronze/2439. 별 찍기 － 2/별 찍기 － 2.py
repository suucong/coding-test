num = int(input())
result = ""

for i in range(1, num + 1):
    for _ in range(num - i):
        result += " "
    for _ in range(i):
        result += "*"
    result += "\n"

print(result)
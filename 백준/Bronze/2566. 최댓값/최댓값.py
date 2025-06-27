matrix = [list(map(int, input().split())) for i in range(9)]
maximum = -1
row, col = 0, 0

for i, l in enumerate(matrix):
    for j, value in enumerate(l):
        if value > maximum:
            maximum = value
            row, col = i + 1, j + 1

print(maximum)
print(f"{row} {col}")
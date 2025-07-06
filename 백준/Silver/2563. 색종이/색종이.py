n = int(input())
paper = [[0] * 101 for _ in range(101)]
coordinates = []
answer = 0
for _ in range(n):
    coordinates.append(tuple(map(int, input().split())))

for coordinate in coordinates:
    for i in range(coordinate[0], coordinate[0] + 10):
        for j in range(coordinate[1], coordinate[1] + 10):
            if paper[i][j] == 0:
                answer += 1
                paper[i][j] = 1

print(answer)



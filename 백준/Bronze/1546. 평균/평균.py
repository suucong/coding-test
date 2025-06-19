num = int(input())
scores = list(map(int, input().split()))

max_score = scores[0]
for i in range(1, num):
    if scores[i] > max_score:
        max_score = scores[i]

sum = 0
for i in range(num):
    sum += scores[i] / max_score * 100

print(sum / num)
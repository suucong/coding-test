kids = [int(input()) for _ in range(9)]
kids.sort()
sum_of_kids = sum(kids)
found = False
for i in range(9):
    for j in range(i + 1, 9):
        cnt = kids[i] + kids[j]
        if (sum_of_kids - cnt) == 100:
            for k in range(9):
                if not (k == i or k == j):
                    print(kids[k])
            found = True
            break
    if found:
        break
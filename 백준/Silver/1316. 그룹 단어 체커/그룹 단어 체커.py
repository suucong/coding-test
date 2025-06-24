num = int(input())
words = []
for _ in range(num):
    words.append(input())

answer = 0
for word in words:
    check_list = {word[0]}
    if len(word) == 1:
        answer += 1
    else:
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:
                if word[i + 1] in check_list:
                    break
                else:
                    check_list.add(word[i + 1])
            if (i + 1) == (len(word) - 1):
                answer += 1

print(answer)
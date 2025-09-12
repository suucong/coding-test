n = int(input())
words = []
char_to_num = {}

for _ in range(n):
    word = input()
    words.append(word)
    for i in range(1, len(word)+1):
        if word[-i] in char_to_num:
            char_to_num[word[-i]] += 10 ** (i - 1)
        else:
            char_to_num[word[-i]] = 10 ** (i - 1)

char_to_num = dict(sorted(char_to_num.items(), key=lambda x: x[1], reverse=True))
num = 9
for key, value in char_to_num.items():
    char_to_num[key] = str(num)
    num -= 1

answer = 0
for word in words:
    num = ''
    for c in word:
        num += char_to_num.get(c)
    answer += int(num)

print(answer)
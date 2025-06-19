word = input()
croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

answer = 0
i = 0
while i < len(word):
    if word[i:i+2] in croatia_alphabet:
        i += 2
    elif word[i:i+3] in croatia_alphabet:
        i += 3
    else:
        i += 1
    answer += 1

print(answer)






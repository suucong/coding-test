N = int(input())
str_list = [input() for _ in range(N)]

str_len = len(str_list[0])
answer = ''

for i in range(str_len):
    first_char = str_list[0][i]
    different_flag = False
    for j in range(1, N):
        if str_list[j][i] != first_char:
            different_flag = True
            break

    if different_flag:
        answer += '?'
    else:
        answer += first_char

print(answer)

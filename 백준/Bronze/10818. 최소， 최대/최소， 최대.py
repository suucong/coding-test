num = int(input())
num_list = list(map(int, input().split()))

min_num = num_list[0]
max_num = num_list[0]

for i in range(1, len(num_list)):
    if num_list[i] > max_num:
        max_num = num_list[i]
    elif num_list[i] < min_num:
        min_num = num_list[i]

result = str(min_num) + " " + str(max_num)
print(result)
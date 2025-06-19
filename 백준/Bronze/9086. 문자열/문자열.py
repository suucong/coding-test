num = int(input())
str_list = []
for i in range(num):
    str_list.append(input())

for word in str_list:
    first_and_last = word[0] + word[-1]
    print(first_and_last)
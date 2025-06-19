nums = list(map(int, input().split()))
nums.sort()

count = 1
duplicated_count = 0
duplicated_num = 0
while count < len(nums):
    if nums[count - 1] == nums[count]:
        duplicated_count += 1
        duplicated_num = nums[count]
    count += 1

price = 0
if duplicated_count == 2:     # 3개의 수가 모두 일치할 때
    price = 10000 + duplicated_num * 1000
elif duplicated_count == 1:     # 2개의 수가 일치할 때
    price = 1000 + duplicated_num * 100
else:
    price = nums[2] * 100

print(price)
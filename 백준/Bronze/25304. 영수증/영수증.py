original_sum = int(input())
products_count = int(input())
products_list = []

for _ in range(products_count):
    a, b = map(int, input().split())
    products_list.append((a, b))

expected_sum = 0
for product in products_list:
    expected_sum += product[0] * product[1]

if expected_sum == original_sum:
    print("Yes")
else:
    print("No")

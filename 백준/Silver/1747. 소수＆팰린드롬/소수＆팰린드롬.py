prime_nums = [1] * 1100001
prime_nums[0] = 0
prime_nums[1] = 0
for i in range(2, 1100001):
    if prime_nums[i] == 1:
        for j in range(i * i, 1100001, i):
            prime_nums[j] = 0

n = int(input())
for k in range(n, 1100001):
    if prime_nums[k] == 1:
        prime_str = str(k)
        for l in range(len(prime_str) // 2):
            if prime_str[l] != prime_str[-1 - l]:
                break
        else:
            print(prime_str)
            break
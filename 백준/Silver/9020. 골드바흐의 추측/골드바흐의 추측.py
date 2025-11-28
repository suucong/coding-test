T = int(input())
test_cases = [int(input()) for _ in range(T)]

is_prime = [True] * (10001)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체
for i in range(2, int(10001 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 10001, i):
            is_prime[j] = False

for t in test_cases:
    for i in range(int(t * 0.5), 1, -1):
        if is_prime[i] and is_prime[t - i]:
            print(i, t - i)
            break

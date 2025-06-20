num = int(input())
real_factors = list(map(int, input().split()))

print(min(real_factors) * max(real_factors))
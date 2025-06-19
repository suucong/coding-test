original_time = list(map(int, input().split()))
required_minutes = int(input())
expected_time = original_time

expected_time[0] = (((original_time[1] + required_minutes) // 60) + original_time[0]) % 24
expected_time[1] = (original_time[1] + required_minutes) % 60

print(" ".join(map(str, expected_time)))
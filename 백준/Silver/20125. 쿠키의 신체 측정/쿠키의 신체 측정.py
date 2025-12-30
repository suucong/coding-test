import sys

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

def find_end_row(start_row, col):
    for i in range(start_row, n):
        if arr[i][col] == '_':
            return i - 1
    return n - 1

heart_loc = None
for i in range(n):
    if '*' in arr[i]:
        head_col = arr[i].find('*')
        heart_loc = (i + 1, head_col)
        print(f'{heart_loc[0] + 1} {heart_loc[1] + 1}')
        break

left_arm = arr[heart_loc[0]][:heart_loc[1]].count('*')
right_arm = arr[heart_loc[0]][heart_loc[1]+1:].count('*')

end_waist = find_end_row(heart_loc[0] + 1, heart_loc[1])
waist_len = end_waist - heart_loc[0]

left_leg = find_end_row(end_waist + 1, heart_loc[1] - 1) - end_waist
right_leg = find_end_row(end_waist + 1, heart_loc[1] + 1) - end_waist

print(f"{left_arm} {right_arm} {waist_len} {left_leg} {right_leg}")
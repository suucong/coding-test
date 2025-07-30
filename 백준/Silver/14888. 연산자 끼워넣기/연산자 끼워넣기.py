N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split())) # +, -, *, //
max_answer = -float('inf')
min_answer = float('inf')

def backtrack(idx, cnt):
    global min_answer, max_answer
    if idx == N:
        max_answer = max(cnt, max_answer)
        min_answer = min(cnt, min_answer)
        return

    if B[0] > 0: # '+'
        B[0] -= 1
        backtrack(idx + 1, cnt + A[idx])
        B[0] += 1

    if B[1] > 0: # '-'
        B[1] -= 1
        backtrack(idx + 1, cnt - A[idx])
        B[1] += 1

    if B[2] > 0: # '*'
        B[2] -= 1
        backtrack(idx + 1, cnt * A[idx])
        B[2] += 1

    if B[3] > 0: # '//'
        B[3] -= 1
        backtrack(idx + 1, cnt // A[idx] if cnt > 0 else -(abs(cnt) // A[idx]))
        B[3] += 1

backtrack(1, A[0])

print(max_answer)
print(min_answer)

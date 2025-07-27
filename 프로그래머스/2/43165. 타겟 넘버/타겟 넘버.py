from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    
    while q:
        current_sum, i = q.popleft()
        
        if i == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            q.append((current_sum + numbers[i], i + 1))
            q.append((current_sum - numbers[i], i + 1))
    
    return answer
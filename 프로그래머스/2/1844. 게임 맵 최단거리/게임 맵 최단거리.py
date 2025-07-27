from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    q = deque()
    q.append((0, 0, 1))
    
    while q:
        x, y, distance = q.popleft()
        
        if 0 <= x < M and 0 <= y < N:
            if maps[y][x] == 1:
                maps[y][x] = 0
                if x == M - 1 and y == N - 1:
                    return distance
                    
                dx = [0, 0, -1, 1]
                dy = [-1, 1, 0, 0]
                for i in range(4):
                    q.append((x + dx[i], y + dy[i], distance + 1))
                        
    return -1
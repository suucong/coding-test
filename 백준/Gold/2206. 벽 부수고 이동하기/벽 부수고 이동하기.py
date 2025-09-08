from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, m, graph):
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    q = deque([(0, 0, 0, 1)])

    while q:
        y, x, broken, dist = q.popleft()
        if (y, x) == (n-1, m-1):
            return dist

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                # 벽이 아니고 아직 방문 안한 경우
                if graph[ny][nx] == 0 and not visited[ny][nx][broken]:
                    visited[ny][nx][broken] = True
                    q.append((ny, nx, broken, dist+1))
                # 벽이고 아직 벽을 부순 적이 없는 경우
                elif graph[ny][nx] == 1 and broken == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    q.append((ny, nx, 1, dist+1))

    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
print(bfs(n, m, graph))


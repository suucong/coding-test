import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, n, graph):
    distances = [INF] * (n + 1)
    pq = [(0, start)]
    distances[start] = 0

    while pq:
        cnt_dist, cnt_node = heapq.heappop(pq)

        if distances[cnt_node] < cnt_dist:
            continue

        for neighbor, weight in graph[cnt_node]:
            new_dist = cnt_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

dist_from_1 = dijkstra(1, n, graph)
dist_from_v1 = dijkstra(v1, n, graph)
dist_from_v2 = dijkstra(v2, n, graph)

# 1 -> v1 -> n
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]

# 1 -> v2 -> n
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)
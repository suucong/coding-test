import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

weights = [float('inf')] * (V + 1)
weights[K] = 0
wq = [(0, K)]

while wq:
    cnt_weight, cnt_node = heapq.heappop(wq)

    if weights[cnt_node] < cnt_weight:
        continue

    for neighbor, weight in graph[cnt_node]:
        weight = cnt_weight + weight

        if weight < weights[neighbor]:
            weights[neighbor] = weight
            heapq.heappush(wq, (weight, neighbor))

for i in range(1, V + 1):
    if weights[i] == float('inf'):
        print('INF')
    else:
        print(weights[i])
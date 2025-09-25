import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, price = map(int, input().split())
    graph[start].append((end, price))
start, end = map(int, input().split())

prices = [float('inf')] * (n + 1)
pq = [(0, start)]
prices[start] = 0

while pq:
    cnt_price, cnt_node = heapq.heappop(pq)

    if prices[cnt_node] < cnt_price:
        continue

    for neighbor, price in graph[cnt_node]:
        price = cnt_price + price

        if price < prices[neighbor]:
            prices[neighbor] = price
            heapq.heappush(pq, (price, neighbor))

print(prices[end])
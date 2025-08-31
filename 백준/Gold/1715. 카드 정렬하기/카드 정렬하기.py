import heapq as hq

n = int(input())
heap = [int(input()) for _ in range(n)]
hq.heapify(heap)

answer = 0

while len(heap) > 1:
    a = hq.heappop(heap)
    b = hq.heappop(heap)
    s = a + b
    answer += s
    hq.heappush(heap, s)

print(answer)
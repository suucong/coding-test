import sys
import heapq as hq

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
heap = []

for v in arr:
    if v == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap, v)
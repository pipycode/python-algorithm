N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

from heapq import heappush, heappop, heapify
heap = [(-table[N-1][i], (N-1, i)) for i in range(N)]
heapify(heap)

for _ in range(N-1):
    x, point = heappop(heap)
    if point[0] > 0:
        heappush(heap, (-table[point[0]-1][point[1]], (point[0]-1, point[1])))
print(-heappop(heap)[0])
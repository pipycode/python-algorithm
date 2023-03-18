from heapq import heappush, heappop

heap = []
for _ in range(int(input())):
    heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    temp = heappop(heap) + heappop(heap)
    result += temp
    heappush(heap, temp)
print(result)
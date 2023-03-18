from heapq import heappop, heappush
N = int(input())

# h1은 maxheap, h2는 minheap
h1, h2 = [], []
result  = []

heappush(h1, -int(input()))
result.append(-h1[0])

for i in range(N-1):
    # 1. 우선 heap에 넣는다.
    number = int(input())
    if number <= -h1[0]:
        heappush(h1, -number)
    else:
        heappush(h2, number)
    # 2. 두 heap의 개수가 같도록 조절한다.
    if len(h1) > len(h2) + 1:
        heappush(h2, -heappop(h1))
    elif len(h1) < len(h2):
        heappush(h1, -heappop(h2))
    # 3. h1의 값을 result로 결정
    result.append(-h1[0])

for i in range(N):
    print(result[i])
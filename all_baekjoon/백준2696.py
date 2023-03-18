from heapq import heappop, heappush

T = int(input())
for _ in range(T):
    M = int(input())
    numbers = []
    for _ in range((M // 10) + 1):
        numbers.extend(list(map(int, input().split())))
    
    low = [-numbers[0]]    # maxheap
    high = []             # minheap
    result = [str(numbers[0])]
    for i, number in enumerate(numbers[1:]):
        if number <= -low[0]:
            heappush(low, -number)
        else:
            heappush(high, number)
        if len(low) < len(high):
            heappush(low, -heappop(high))
        elif len(low) > len(high) + 1:
            heappush(high, -heappop(low))
        
        if i % 2 == 1:
            result.append(str(-low[0]))
    
    print(len(result))
    for i, number in enumerate(result):
        if i!=0 and i%10==0:
            print('\n' + number, end=' ')
        else:
            print(number, end=' ')
    print()
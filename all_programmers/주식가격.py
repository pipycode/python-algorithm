from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    
    q = deque()
    for i, price in enumerate(prices):
        if len(q) == 0 or q[len(q) - 1][1] <= price:
            q.append([i, price])
        else:
            while len(q) != 0 and q[len(q) - 1][1] > price:
                top = q.pop()
                answer[top[0]] = i - top[0]
            q.append([i, price])
    while q:
        top = q.pop()
        answer[top[0]] = len(prices) - 1 - top[0]
                
    return answer
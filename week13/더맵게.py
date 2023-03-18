import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        non_spicy1 = heapq.heappop(scoville)
        non_spicy2 = heapq.heappop(scoville)
        mix_spicy = non_spicy1 + (non_spicy2 * 2)
        heapq.heappush(scoville, mix_spicy)
        answer += 1
    
    return answer
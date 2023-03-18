from collections import Counter, deque
def solution(priorities, location):
    answer = 0
    document_num = Counter(priorities)
    q = deque(priorities)
    
    while q:
        now = q.popleft()
        
        printing = True
        for i in range(now + 1, 10):
            if document_num[i] > 0:
                printing = False
        
        if printing:
            document_num[now] -= 1
            answer += 1            
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            q.append(now)
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1
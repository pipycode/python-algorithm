# 방향설정
dx = (1, 0, -1)
dy = (0, 1, -1)
from itertools import chain
def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    
    now = [0, 0]
    direct = 0
    num = 1
    
    while num <= (n * (n + 1) // 2):
        answer[now[0]][now[1]] = num
        nxt = [now[0] + dx[direct], now[1] + dy[direct]]
        if nxt[0] >= len(answer) or nxt[1] >= len(answer[nxt[0]]) or answer[nxt[0]][nxt[1]]:
            direct = (direct + 1) % 3
        nxt = [now[0] + dx[direct], now[1] + dy[direct]]
        now = nxt
        num += 1
        
    return list(chain(*answer))
# extra, idea
FIRST = [input().split() for _ in range(3)]
from itertools import permutations
visited = {}

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def _nxt(now:str, zero):
    result = []
    for i in range(4):
        nxt = [zero[0]+di[i], zero[1]+dj[i]]
        if 0<=nxt[0]<3 and 0<=nxt[1]<3:
            arr = [list(now[:3]), list(now[3:6]), list(now[6:])]
            arr[zero[0]][zero[1]] = arr[nxt[0]][nxt[1]]
            arr[nxt[0]][nxt[1]] = '0'
            result.append([''.join([''.join(arr[i]) for i in range(3)]), nxt])
    return result
            
from collections import deque
def BFS(start:str, zero:list):
    num = 0
    q = deque([[start, zero]])
    visited[start] = True
    while q:
        s = len(q)
        for _ in range(s):
            now, zero = q.popleft()
            if now == '123456780':
                return num
            for nxt, nxt_zero in _nxt(now, zero):
                if not visited.get(nxt):
                    visited[nxt] = True
                    q.append([nxt, nxt_zero])
        num +=1
    return -1

for i in range(3):
    for j in range(3):
        if FIRST[i][j] == '0':
            zero = (i, j)
print(BFS(''.join([''.join(FIRST[i]) for i in range(3)]), zero))
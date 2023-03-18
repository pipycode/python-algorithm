# 1. 현재 가지고 있는 열쇠로 열 수 있는 문을 모두 없앤다.
# 2. 문을 없앤 후 가져올 수 있는 열쇠/문서들을 가져온다.
# 3. 모든 문서를 가져오거나 더이상 문을 없앨 수 없을 때 그만둔다.

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

from collections import deque
def BFS(BUILDING, KEYS, start_point, H, W):
    visited = [[False]*W for _ in range(H)]
    start_i, start_j = start_point
    result = 0
    q = deque()
    q.append([start_i, start_j])
    visited[start_i][start_j] = True
    while q:
        now = q.popleft()
        for i in range(4):
            nxt = (now[0]+di[i], now[1]+dj[i])
            if 0<= nxt[0] < H and 0<= nxt[1] <W and BUILDING[nxt[0]][nxt[1]] != '*':
                # 방문하지 않고, .인 부분은 지나칠 수 있음
                if BUILDING[nxt[0]][nxt[1]] == '.':
                    if not visited[nxt[0]][nxt[1]]:
                        visited[nxt[0]][nxt[1]] = True
                        q.append(nxt)
                # 방문하지 않고 $인 부분은 문서를 훔침
                elif BUILDING[nxt[0]][nxt[1]] == '$':
                    if not visited[nxt[0]][nxt[1]]:
                        visited[nxt[0]][nxt[1]] = True
                        q.append(nxt)
                        result += 1
                # 방문하지 않고 열쇠를 가지고 있는 곳은 열쇠를 획득할 수 있음 
                elif BUILDING[nxt[0]][nxt[1]].islower():
                    if not visited[nxt[0]][nxt[1]]:
                        visited[nxt[0]][nxt[1]] = True
                        q.append(nxt)
                        if BUILDING[nxt[0]][nxt[1]].upper() not in KEYS:
                            KEYS.append(BUILDING[nxt[0]][nxt[1]].upper())
                # 방문하지 않고 열쇠를 가지고 있는 문은 지나칠 수 있음
                else:
                    if not visited[nxt[0]][nxt[1]] and BUILDING[nxt[0]][nxt[1]] in KEYS:
                        visited[nxt[0]][nxt[1]] = True
                        q.append(nxt)
    return result

N = int(input())
results = []
for _ in range(N):
    H, W = map(int, input().split())
    BUILDING = [[] for _ in range(H+2)]
    BUILDING[0], BUILDING[H+1] = ['.'] * (W+2), ['.'] * (W+2)
    for i in range(1, H+1):
        BUILDING[i] = ['.'] + list(input()) + ['.']
    KEYS = []
    KEY = list(input())
    if KEY[0] != '0':
        KEYS.extend(list(map(lambda x:x.upper(), KEY)))

    # key의 개수가 변하지 않을 때까지 반복 가능    
    base = -1
    while len(KEYS) != base:
        base = len(KEYS)
        result = BFS(BUILDING, KEYS, (0, 0), H+2, W+2)
    results.append(result)

for result in results:
    print(result)
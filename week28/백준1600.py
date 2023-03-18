INF = 200*200+1
K = int(input())
W, H = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(H)]

from collections import deque
monkey_di = (-1, 0, 1, 0)
monkey_dj = (0, 1, 0, -1)
horse_di = (-2, -1, 1, 2, 2, 1, -1, -2)
horse_dj = (1, 2, 2, 1, -1, -2, -2, -1)

def BFS(start):
    # distance[i][j][k]는 말 움직임을 K번 사용해서 i,j로 움직일때 최소 거리
    distance = [[[INF] * (K+1) for _ in range(W)] for _ in range(H)]
    distance[start[0]][start[1]] = [0]*(K+1)
    q = deque([start])
    while q:
        now = q.popleft()
        # monkey step
        for i in range(4):
            nxt = (now[0] + monkey_di[i], now[1] + monkey_dj[i])
            if 0<=nxt[0]<H and 0<=nxt[1]<W and not world[nxt[0]][nxt[1]]:
                check = False
                for k in range(K+1):
                    if distance[nxt[0]][nxt[1]][k] > distance[now[0]][now[1]][k] + 1:
                        distance[nxt[0]][nxt[1]][k] = distance[now[0]][now[1]][k] + 1
                        check = True
                if check:
                    q.append(nxt)
        # horse step
        for i in range(8):
            nxt = (now[0] + horse_di[i], now[1] + horse_dj[i])
            if 0<=nxt[0]<H and 0<=nxt[1]<W and not world[nxt[0]][nxt[1]]:
                check = False
                for k in range(1, K+1):
                    if distance[nxt[0]][nxt[1]][k] > distance[now[0]][now[1]][k-1] + 1:
                        distance[nxt[0]][nxt[1]][k] = distance[now[0]][now[1]][k-1] + 1
                        check = True
                if check:
                    q.append(nxt)
    return min(distance[H-1][W-1])

result = BFS((0, 0))
if result>=INF:
    print(-1)
else:
    print(result)
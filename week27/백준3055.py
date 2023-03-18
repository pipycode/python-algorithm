from collections import deque
def simulation(forest:list, hedgehog:list, water:list):
    # hedgehog: 고슴도치의 처음 위치
    # water: 물의 처음 위치(모든 물에 대해)
    visited = [[False]*len(forest[0]) for _ in range(len(forest))]
    visited[hedgehog[0]][hedgehog[1]] = True
    hedgehog = deque([hedgehog])
    temp = deque()
    for w in water:
        visited[w[0]][w[1]] = True
        temp.append(w)
    water = temp
    time = 0
    while hedgehog:
        time += 1
        # 고슴도치가 못가는 곳을 알기 위해 물 먼저 이동
        s_w = len(water)
        for _ in range(s_w):
            now = water.popleft()
            for i in range(4):
                nxt = [now[0]+di[i], now[1]+dj[i]]
                if 0<=nxt[0]<len(forest) and 0<=nxt[1]<len(forest[0]) and not visited[nxt[0]][nxt[1]]:
                    # 돌과 물이 없는 곳으로 이동 가능
                    if forest[nxt[0]][nxt[1]] == '.':
                        water.append(nxt)
                        visited[nxt[0]][nxt[1]] = True
                        forest[nxt[0]][nxt[1]] = '*'
        # 고슴도치 이동
        s_h = len(hedgehog)
        for _ in range(s_h):
            now = hedgehog.popleft()
            for i in range(4):
                nxt = [now[0]+di[i], now[1]+dj[i]]
                if 0<=nxt[0]<len(forest) and 0<=nxt[1]<len(forest[0]) and not visited[nxt[0]][nxt[1]]:
                    # 돌과 물이 없는 곳으로 이동 가능
                    if forest[nxt[0]][nxt[1]] == '.':
                        hedgehog.append(nxt)
                        visited[nxt[0]][nxt[1]] = True
                    # 만약 비버의 집으로 갈 수 있으면 True반환
                    elif forest[nxt[0]][nxt[1]] == 'D':
                        return time

    # 갈 수 있는 곳을 전부 갔음에도 비버의 집에 도착할 수 없었으면 False
    return 'KAKTUS'

R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# water[t]: t초에 water의 가장자리위치 저장
water = []
for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            water.append([i, j])
        elif forest[i][j] == 'S':
            hedgehog = [i, j]
        elif forest[i][j] == 'D':
            beaver = [i, j]
if abs(beaver[0]-hedgehog[0]) + abs(beaver[1]-hedgehog[1]) == 1:
    print(1)
else:
    print(simulation(forest, hedgehog, water))
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
for i in range(R):
    if room[i][0] == -1:
        cleaner_i = i
        break

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def diffuse():
    # 확산 장소와 양 먼저 계산
    diffuse_point = []
    for i in range(R):
        for j in range(C):
            if room[i][j] <= 0:
                continue
            diffuse_num = 0
            diffuse_quantity = room[i][j] // 5
            for k in range(4):
                new_i, new_j = i + dr[k], j+dc[k]
                if 0<=new_i<R and 0<=new_j<C and room[new_i][new_j]!=-1:
                    diffuse_num += 1
                    diffuse_point.append((new_i, new_j, diffuse_quantity))
            room[i][j] = room[i][j] - (diffuse_quantity * diffuse_num)
    # 확산
    for i, j, dust in diffuse_point:
        room[i][j] += dust

def air_cleaner():
    # 위쪽 cleaner
    up = [cleaner_i, 1]
    direction = 1
    past_dust = 0
    while not (up[0]==cleaner_i and up[1]==0):
        if 0<=up[0]+dr[direction]<R and 0<=up[1]+dc[direction]<C:
            now_dust = room[up[0]][up[1]]
            room[up[0]][up[1]] = past_dust
            past_dust = now_dust
            up[0] += dr[direction]
            up[1] += dc[direction]
        else:
            direction = (direction - 1) % 4

    # 아래쪽 cleaner
    down = [cleaner_i+1, 1]
    direction = 1
    past_dust = 0
    while not (down[0]==cleaner_i+1 and down[1]==0):
        if 0<=down[0]+dr[direction]<R and 0<=down[1]+dc[direction]<C:
            now_dust = room[down[0]][down[1]]
            room[down[0]][down[1]] = past_dust
            past_dust = now_dust
            down[0] += dr[direction]
            down[1] += dc[direction]
        else:
            direction = (direction + 1) % 4

for _ in range(T):
    diffuse()
    air_cleaner()
    
print(sum([sum(room[i]) for i in range(R)]) + 2)
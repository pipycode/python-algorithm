import copy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1 , 1]

# 물고기 번호가 0 이면 상어 -1이면 빈칸
fish = []

for i in range(4):
    row = list(map(int, input().split()))
    temp = []
    
    for j in range(0,len(row),2):
        temp.append(row[j:j+2])
    
    fish.append(temp)

# fish[물고기가 위치한 칸의 행 번호][... 열 번호][0] : 물고기 번호
# fish[... 행 번호][... 열 번호][1] : 물고기의 방향

ans = 0
position = []

# 반환 값이 0이면 상어는 집에 가야하는 상태이므로 물고기 번호의 합의 최댓값을 출력한다.
def shark_move(n, x, y,direction):
    global ans, position
    cnt = 0
    
    if 3 <= x or 3 <= y:
        return 0
    
    cnt += fish[x][y][0]
    ans = max(ans, cnt)
    if n and ans == cnt:
        print(cnt, ans)
        position.append((x,y))
    
    nx, ny = x + dx[direction-1], y + dy[direction-1]
    if 4 > nx or 4 > ny:
        shark_move(n + 1, nx, ny, direction)
    
    
    # 상어가 한번 움직였을 때 먹을 수 있는 물고기 번호의 최댓값, 움직인 상어의 좌표
    return ans, position

# 크기가 작은 물고기부터 이동하기 때문
def fish_sort():
        tmp = []
        for i in range(4):
            for j in range(4):
                tmp.append((i,j,fish[i][j][0],fish[i][j][1]))
            
        tmp.sort(key = lambda x :(x[2]))
        return tmp
    
# 이동 전 위치, 물고기 번호, 이동 방향
def fish_move(x, y, num, direction):
    if fish[x][y][0] == 0:
        return
    
    cnt = 0
    while cnt < 4:
        nx, ny = x + dx[direction-1],  y + dy[direction-1]
        if nx > 3 or ny > 3:
            direction -= 1
            cnt += 1
        
        else:
            if fish[nx][ny] != 0:
                fish[nx][ny][0], fish[x][y][0] = fish[x][y][0], fish[nx][ny][0]
                fish[nx][ny][1], fish[x][y][1] = fish[x][y][0], direction
                return
            
    


# num은 방향
def solution(n,x,y,direction):
    
    new_n,new_x,new_y,new_direction = n,x,y,direction
            
    result = 0
    while True:
        if not shark_move(new_n,new_x,new_y,new_direction):
            break
        
        else:
            cnt, new_shark_position = shark_move(new_n,new_x,new_y,new_direction)
            fish[new_shark_position[0]][new_shark_position[1]][0] = -1
            result += cnt
            
    
        for f in fish_sort():
            fish_move(*f)
            
        new_n,new_x,new_y,new_direction = new_shark_position[0], new_shark_position[1], fish[new_shark_position[0]][new_shark_position][1]
        fish[new_shark_position[0]][new_shark_position[1]][0] = 0


    return cnt
    
print(solution(0,0,0,fish[0][0][1]))

    
    
        
    

        

    
import copy, sys
input = sys.stdin.readline

fish = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    
    for j in range(4):
        fish[i][j] = [data[j * 2], data[j * 2 + 1] -1]
        
        
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    return (direction + 1) % 8

def find_fish_index(fish, index):
    for i in range(4):
        for j in range(4):
            if fish[i][j][0] == index:
                return (i,j)
            
    return None
    

def move_all_fish(fish, now_x, now_y):
    for i in range(17):
        position = find_fish_index(fish, i)
        
        if position != None:
            x, y = position[0], position[1]
            direction = fish[x][y][1]
            
            for i in range(8):
                nx, ny = x + dx[direction], y + dy[direction]
                
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not(nx == now_x and ny == now_y):
                        fish[x][y][1] = direction
                        fish[x][y], fish[nx][ny] = fish[nx][ny], fish[x][y]
                        break
                
                
                direction = turn_left(direction)
            
def get_possible_positions(fish, now_x, now_y):
    positions = []
    direction = fish[now_x][now_y][1]
    
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if fish[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
   
    return positions
                
                        
    

ans = 0
def dfs(fish, now_x, now_y, total):
    global ans
    tmp = copy.deepcopy(fish)
    
    total += tmp[now_x][now_y][0]
    tmp[now_x][now_y][0] = -1
    
    move_all_fish(tmp, now_x, now_y)
    positions = get_possible_positions(tmp, now_x, now_y)
    
    if len(positions) == 0:
        ans = max(ans, total)
        return 
    
    for next_x, next_y in positions:
        dfs(tmp, next_x, next_y, total)
        
dfs(fish, 0, 0, 0)
print(ans)
        
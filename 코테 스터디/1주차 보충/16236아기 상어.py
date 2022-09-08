from collections import deque
from sys import maxsize

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_x, shark_y = 0, 0



for i in range(n):
    for j in range(n):
        # 아기 상어의 초기 좌표 찾기
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            
            # 아기 상어의 칸이 9로 되어있으면 
            # 상어가 해당 칸을 지나지 못하므로 0으로 초기화 해준다.
            graph[i][j] = 0
    
            
def bfs():
    global shark_x, shark_y, cnt
    
    queue = deque([(shark_x, shark_y)])
    visited = [[-1] * n for _ in range(n)]
    
    visited[shark_x][shark_y] = 0
    min_dist = maxsize
    
    fish = []
    
    while queue:
        x, y = queue.popleft()
        
        # 상어로부터 가까운 칸에서부터 탐색하면서, 상어가 해당 칸에 물고기를 먹을 수 있는지 확인한다.
        # 상어는 자기보다 작은 물고기를 먹을 수 있다.
        if 0 < graph[x][y] < size:
            min_dist = min(min_dist, visited[x][y])
            
            if min_dist == visited[x][y]:
                fish.append((x,y))
            else:
                break
        
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] <= size and visited[nx][ny] == -1:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
    if fish:
        # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다
        fish.sort()
        x,y = fish[0]
        
        shark_x, shark_y, cnt = x, y, cnt + 1
        graph[x][y] = 0
        
        return min_dist

    else:
        return None      
        
# 최종 결과값
ans = 0

# 상어의 사이즈와 물고기를 먹은 횟수
size, cnt = 2, 0
                
while True:
    sec = bfs()
    
    if sec == None:
        break
    
    ans += sec
    
    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다
    if cnt == size:
        size += 1
        cnt = 0
        

print(ans)
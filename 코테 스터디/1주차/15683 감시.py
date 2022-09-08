import copy

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
} # cctv 종류에 따른 감시 방향
                        

def watch(x,y,direction,tmp):
    
    for d in direction:
        nx, ny = x, y
        
        while True:
            nx += dx[d]
            ny += dy[d]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or tmp[nx][ny] == 6:
                break
            
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = '#'
            

def dfs(n,graph):
    global ans
    tmp = copy.deepcopy(graph)
    
    # cctv를 모두 탐색했으면
    if n == len(cctv):
        # 사각지대의 개수
        count = 0
        for t in tmp:
            count += t.count(0)
        
        ans = min(ans, count)
        return
        
    x, y, c = cctv[n]
    
    for d in direction[c]:
        watch(x,y,d,tmp)
        dfs(n+1,tmp)
        tmp = copy.deepcopy(graph)
        

cctv = []    
ans = 1e9


for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append([i,j,graph[i][j]])
        

dfs(0,graph)
print(ans)
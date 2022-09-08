import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
result = 0

def dfs(x, y, sum, depth):
    global result
    
    if depth == 4:
        result = max(result, sum)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, sum +  paper[nx][ny], depth + 1)
                visited[nx][ny] = False
                
                
def exception(x,y):
    global result
    
    # ㅓ, ㅏ ㅗ, ㅜ 4종류
    for i in range(4):
        tmp = paper[x][y]
        
        for j in range(3):
            k = (i + j) % 4
            
            nx, ny = x + dx[k], y + dy[k]
            
            if not (0 <= nx < 4 and 0 <= ny < 4):
                tmp = 0
                break
            
            tmp += paper[nx][ny]
        
        result = max(result, tmp)
        
                


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,0,0)
        visited[i][j] = False
        
        exception(i,j)
        
print(result)

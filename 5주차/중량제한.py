from unittest import result


n, m = map(int, input().split())
adj = [ [] for i in range(n+1)]
first = 10000000
last = 1
start, end = map(int,input().split())
results = first

def bfs(c):
    que = [start]
    visited = [False] * (n+1)
    visited[start] = True

    while que:
        x = que.pop(0)
        for y, weight in adj[x]:
            if not visited[y] and weight >= c: # 만약 y를 방문하지 않았고 중량이 초과되지 않는다면 방문함
                visited[y] = True
                que.append()
    return visited[end]

for i in range(m):
    x,y,weight = map(int, input().split())
    adj[x].append((y,weight)) # 양방향이라서 다리에 서로의 점 정보 추가
    adj[y].append((x,weight))
    first = min(first, weight) # 최소 중량
    last = max(last, weight) # 최대 중량


while(first <=last): # 이분탐색
    mid = (first + last) // 2
    if bfs(mid):
        results = mid
        first = mid + 1
    else:
        last = mid - 1


print(results)
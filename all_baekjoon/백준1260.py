N, M, V = map(int, input().split())

CON = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    CON[x].append(y)
    CON[y].append(x)
for i in range(N+1):
    CON[i].sort()

def DFS(now, visited):
    print(now, end=' ')
    visited[now] = True
    for nxt in CON[now]:
        if not visited[nxt]:
            DFS(nxt, visited)

from collections import deque
def BFS(now, visited):
    q = deque([now])
    visited[now] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for nxt in CON[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

visited = [False] * (N+1)
DFS(V, visited)
print()
visited = [False] * (N+1)
BFS(V, visited)
print()
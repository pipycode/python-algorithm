Node_num, test_num = map(int, input().split())

INF = 2001
Node = [[] for _ in range(1001)]
for _ in range(Node_num - 1):
    x, y, d = map(int, input().split())
    Node[x].append([y, d])
    Node[y].append([x, d])

from collections import deque    
def bfs_distance(start, end):
    q = deque()
    visited = [False] * 1001
    
    q.append([start, 0])
    visited[start] = True
    
    while q:
        s = len(q)
        for _ in range(s):
            now, dist = q.popleft()
            nxt = [(nxt, d) for nxt, d in Node[now] if not visited[nxt]]
            for n, d in nxt:
                if n == end:
                    return dist + d
                else:
                    q.append([n, dist + d])
                    visited[n] = True
                    

for _ in range(test_num):
    start, end = map(int, input().split())
    print(bfs_distance(start, end))
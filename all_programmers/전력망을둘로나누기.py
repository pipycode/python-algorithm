# 2 <= n <= 100
# 1. BruteForce가능 (최대 100번만 해보면 되기 때문)
from collections import deque

def bfs(start, do_not, visited, Map):
    num = 1
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for next in Map[now]:
            if not visited[next] and next != do_not:
                visited[next] = True
                q.append(next)
                num += 1
    return num    

def solution(n, wires):
    answer = 100
    Map = [[] for i in range(n + 1)]
    for x, y in wires:
        Map[x].append(y)
        Map[y].append(x)
    
    for i, remove in enumerate(wires):
        visited = [False] * (n + 1)
        x = bfs(remove[0], remove[1], visited, Map)
        y = bfs(remove[1], remove[0], visited, Map)
        if answer > abs(x-y):
            answer = abs(x-y)
    return answer
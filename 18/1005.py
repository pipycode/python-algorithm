from collections import deque
import copy
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    b_time = list(map(int, input().split()))
    graph_go = [[] for __ in range(n)]
    graph_come = [[] for __ in range(n)]
    entry_level = [0] * n
    for __ in range(k):
        p, q = map(int, input().split())
        q -= 1
        p -= 1
        entry_level[q] += 1
        graph_go[p].append(q)
        graph_come[q].append(p)
    w = int(input())
    w -= 1
    sorted_q = deque()
    visited = [False] * n
    while False in visited:
        que = deque()
        for i in range(n):
            if entry_level[i] <= 0 and not visited[i]:
                que.append(i)
                visited[i] = True
        while que:
            node = que.popleft()
            for des in graph_go[node]:
                entry_level[des] -= 1
            sorted_q.append(node)
    dp = [0] * n
    for qs in sorted_q:
        for come in graph_come[qs]:
            dp[qs] = max(dp[qs], dp[come])
        dp[qs] += b_time[qs]
        if w == qs:
            print(dp[qs])





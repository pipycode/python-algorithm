V = int(input())

# 1을 root로 만들 것
tree_INFO = [[] for _ in range(V+1)]
for _ in range(V):
    info = list(map(int, input().split()))
    for i in range(1, len(info)-1, 2):
        nxt, cost = info[i], info[i+1]
        tree_INFO[info[0]].append((nxt, cost))

dist_INFO = [0] * (V+1)

# 빽트래킹, start를 기준으로 가장 긴 가지의 길이 return
def DFS(start, visited, cost):
    visited[start] = True
    # leaf Node일 경우 가지 길이 return
    if len(tree_INFO[start]) == 1 and visited[tree_INFO[start][0][0]]:
        return cost
    
    # leaf Node가 아닐 경우
    length = []
    for nxt, c in tree_INFO[start]:
        if not visited[nxt]:
            length.append(DFS(nxt, visited, c))
    length.sort()
    if len(length) == 0:
        dist_INFO[start] = 0
    elif len(length) == 1:
        dist_INFO[start] = length[0]
    else:
        dist_INFO[start] = length[len(length)-1] + length[len(length)-2]
    return length[len(length)-1] + cost

visited = [False for _ in range(V+1)]
DFS(1, visited, 0)
print(max(dist_INFO))
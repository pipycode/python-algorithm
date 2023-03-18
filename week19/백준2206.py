N, M = map(int, input().split())
wall = [input() for _ in range(N)]

# BFS
# 현재위치 -> (거리, 부순횟수) -> 다음위치

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
from collections import deque
def BFS(N, M, wall):
    if N == 1 and M == 1:
        return 1
    # now_x, now_y, dist, breaking
    q = deque([[0, 0, 1, 0]])
    # best[i][j][0], best[i][j][1]
    # : breaking이 0일때 최소거리 ,breaking이 1일때 최소거리
    best = [[[1000 * 1000, 1000 * 1000] for _ in range(M)] for _ in range(N)]
    best[0][0][0], best[0][0][1] = 1, 1
    while q:
        s = len(q)
        for i in range(s):
            now_x, now_y, dist, breaking = q.popleft()
            for i in range(4):
                nxt_x = now_x + dx[i]
                nxt_y = now_y + dy[i]
                if nxt_x < 0 or nxt_x >=N or nxt_y < 0 or nxt_y >= M:
                    continue
                if nxt_x == N-1 and nxt_y == M-1:
                    return dist + 1
                if wall[nxt_x][nxt_y] == '0':
                    # break의 수는 같으나 dist가 더 길면 제외
                    if best[nxt_x][nxt_y][breaking] <= dist+1:
                        continue
                    q.append([nxt_x, nxt_y, dist+1, breaking])
                    best[nxt_x][nxt_y][breaking] = dist+1
                else:
                    if breaking == 1:
                        continue
                    # break의 수는 같으나 dist가 더 길면 제외
                    if best[nxt_x][nxt_y][breaking] <= dist+1:
                        continue
                    q.append([nxt_x, nxt_y, dist+1, breaking+1])
                    best[nxt_x][nxt_y][breaking] = dist+1
    return -1

print(BFS(N, M, wall))
# DFS 빽트래킹
N = int(input())
HOME = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0] * 3 for _ in range(N)] for _ in range(N)]

def _nxt(start, direction):
    i, j = start[0], start[1]
    # 시작이 가로일 경우
    if direction == 0:
        if  (0<=i+1<N and 0<=j+1<N) and (not HOME[i+1][j+1] and not HOME[i+1][j] and not HOME[i][j+1]):
            return [((i, j+1), 0), ((i+1, j+1), 2)]
        elif (0<=j+1<N) and not HOME[i][j+1]:
            return [((i, j+1), 0)]
    # 시작이 세로일 경우
    elif direction == 1:
        if (0<=i+1<N and 0<=j+1<N) and (not HOME[i+1][j] and not HOME[i+1][j+1] and not HOME[i][j+1]):
            return [((i+1, j), 1), ((i+1, j+1), 2)]
        elif (0<=i+1<N) and not HOME[i+1][j]:
            return [((i+1, j), 1)]
    # 시작이 대각선일 경우:
    elif direction == 2:
        if (0<=i+1<N and 0<=j+1<N) and (not HOME[i+1][j] and not HOME[i+1][j+1] and not HOME[i][j+1]):
            return [((i, j+1), 0), ((i+1, j), 1), ((i+1, j+1), 2)]
        elif (0<=i+1<N and 0<=j+1<N) and (not HOME[i][j+1] and not HOME[i+1][j]):
            return [((i, j+1), 0), ((i+1, j), 1)]
        elif (0<=j+1<N) and not HOME[i][j+1]:
            return [((i, j+1), 0)]
        elif (0<=i+1<N) and not HOME[i+1][j]:
            return [((i+1, j), 1)]
    return None

def DFS(now, direction):
    if now == (N-1, N-1):
        return 1
    elif DP[now[0]][now[1]][direction] < 0:
        return 0
    elif DP[now[0]][now[1]][direction] > 0:
        return DP[now[0]][now[1]][direction]
    elif DP[now[0]][now[1]][direction] == 0:
        result = 0
        nxt = _nxt(now, direction)
        if nxt is not None:
            for nxt_point, nxt_direction in nxt:
                if 0<=nxt_point[0]<N and 0<=nxt_point[1]<N:
                    result += DFS(nxt_point, nxt_direction)
            DP[now[0]][now[1]][direction] = result
        else:
            DP[now[0]][now[1]][direction] = -1
        return result

if HOME[N-1][N-1] == 1:
    print(0)
else:
    print(DFS((0,1), 0))
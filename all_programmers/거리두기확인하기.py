from collections import deque

nxt = ((-1, 0), (0, 1), (1, 0), (0, -1))
def bfs(MAP, start, VISITED):
    q = deque()
    q.append(start)
    VISITED[start[0]][start[1]] = True
    dst = 1
    while q and dst <= 2:
        for _ in range(len(q)):
            now_visit = q.popleft()
            for i in range(4):
                next_visit = [now_visit[0] + nxt[i][0], now_visit[1] + nxt[i][1]]
                if next_visit[0] < 0 or next_visit[0] >= 5:
                    continue
                if next_visit[1] < 0 or next_visit[1] >= 5:
                    continue
                if MAP[next_visit[0]][next_visit[1]] == 'X':
                    continue
                if VISITED[next_visit[0]][next_visit[1]]:
                    continue
                if MAP[next_visit[0]][next_visit[1]] == 'P':
                    print(now_visit, next_visit)
                    return False
                VISITED[next_visit[0]][next_visit[1]] = True
                q.append([next_visit[0], next_visit[1]])
        dst += 1
    return True

def solution(places):
    answer = []
    for MAP in places:
        print(MAP)
        check = 1
        VISITED = [[False]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if check and MAP[i][j] == 'P'and not bfs(MAP, [i, j], VISITED):
                        check = 0
        answer.append(check)
    return answer
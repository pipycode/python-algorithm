n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s_n = 0
for line in board:
    s_n = max(s_n, max(line))
s_m = list(map(int, input().split()))
move = [[list(map(int, input().split())) for _ in range(4)] \
        for sk in range(s_n)]
board_smell = [[[0, 0]] * n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ret = 0
while True:
    for i in range(n):
        for j in range(n):
            if board_smell[i][j][0] > 0:
                board_smell[i][j][0] -= 1
            if board[i][j] != 0:
                board_smell[i][j] = [k, board[i][j]]
    new_board = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if 0 != board[r][c]:
                see = board[r][c]
                is_moving = False
                #단어 다시 최신화
                for order in move[see - 1][s_m[see - 1] - 1]:
                    #print(see)
                    nr = r + dr[order-1]
                    nc = c + dc[order-1]
                    if 0 <= nr < n and 0 <= nc < n:
                        if board_smell[nr][nc][0] == 0:
                            if new_board[nr][nc] != 0 and new_board[nr][nc] < board[r][c]:
                                board[r][c] = 0
                            else:
                                new_board[nr][nc] = board[r][c]
                                board[r][c] = 0
                            is_moving = True
                            s_m[see - 1] = order
                            break
                #자신의 길을 되돌아가야함
                if not is_moving:
                    for tmp in move[see - 1][s_m[see - 1] - 1]:
                        i = tmp - 1
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < n and 0 <= nc < n and board_smell[nr][nc][1] == board[r][c]:
                            if new_board[nr][nc] != 0 and new_board[nr][nc] < board[r][c]:
                                board[r][c] = 0
                            else:
                                new_board[nr][nc] = board[r][c]
                                board[r][c] = 0
                            s_m[see - 1] = i + 1
                            break

    board = new_board
    ret += 1
    is_end = True
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                is_end = False
    if is_end:
        print(ret)
        break
    if ret >= 1000:
        print(-1)
        break

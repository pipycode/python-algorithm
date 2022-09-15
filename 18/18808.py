n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
def sti():
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    for i in range(4):
        #회전 회오리 부분
        for s_r in range(n - r + 1):
            for s_c in range(m - c + 1):
                please_stop = False
                for can_r in range(r):
                    for can_c in range(c):
                        if sticker[can_r][can_c] == 1 and \
                             board[s_r + can_r][s_c + can_c] == 1:
                            please_stop = True
                            break
                if not please_stop:
                    for can_r in range(r):
                        for can_c in range(c):
                            if sticker[can_r][can_c] == 1 and \
                                board[s_r + can_r][s_c + can_c] == 0:
                                board[s_r + can_r][s_c + can_c] = sticker[can_r][can_c]
                    return
        new_stick = []
        for c_i in range(c):
            tmp = []
            for r_i in range(r - 1, -1, -1):
                #print(sticker, r_i, c_i)
                tmp.append(sticker[r_i][c_i])
            new_stick.append(tmp)
        sticker = new_stick
        r, c = c, r
cnt = 0
for _ in range(k):
    sti()
for nn in range(n):
    cnt += board[nn].count(1)

print(cnt)

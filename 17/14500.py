def o_1(x, y, monun):
    if len(monun[0]) <= x + 3:
        return 0
    return monun[y][x] + monun[y][x + 1] + monun[y][x + 2] + monun[y][x + 3]
def o_2(x, y, monun):
    if len(monun) <= y + 3:
        return 0
    return monun[y][x] + monun[y + 1][x] + monun[y + 2][x] + monun[y + 3][x]
def t_1(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y][x] + monun[y + 1][x] + monun[y][x + 1] + monun[y + 1][x + 1]
def th_1(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x] + monun[y + 1][x] + monun[y + 2][x] + monun[y + 2][x + 1]
def th_2(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y + 1][x] + monun[y + 1][x + 1] + monun[y + 1][x + 2] + monun[y][x + 2]
def th_3(x, y, monun):#ㄱ
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x] + monun[y][x + 1] + monun[y + 1][x + 1] + monun[y + 2][x + 1]
def th_4(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y][x] + monun[y + 1][x] + monun[y][x+1] + monun[y][x + 2]
def f_1(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x] + monun[y + 1][x] + monun[y + 1][x + 1] + monun[y + 2][x + 1]
def f_2(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y + 1][x] + monun[y + 1][x + 1] + monun[y][x + 1] + monun[y][x + 2]
def f_3(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x + 1] + monun[y + 1][x + 1] + monun[y + 1][x] + monun[y + 2][x]
def f_4(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y][x] + monun[y][x + 1] + monun[y + 1][x + 1] + monun[y + 1][x + 2]
def s_1(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y][x] + monun[y][x + 1] + monun[y][x + 2] + monun[y + 1][x + 1]
def s_2(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y + 1][x] + monun[y + 1][x + 1] + monun[y + 1][x + 2] + monun[y][x + 1]
def s_3(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x] + monun[y + 1][x] + monun[y + 2][x] + monun[y + 1][x + 1]
def s_4(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x + 1] + monun[y + 1][x + 1] + monun[y + 2][x + 1] + monun[y + 1][x]
def sv_1(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x + 1] + monun[y + 1][x + 1] + monun[y + 2][x + 1] + monun[y + 2][x]
def sv_2(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y][x] + monun[y][x + 1] + monun[y][x + 2] + monun[y + 1][x + 2]
def sv_3(x, y, monun):
    if len(monun[0]) <= x + 1:
        return 0
    if len(monun) <= y + 2:
        return 0
    return monun[y][x] + monun[y][x + 1] + monun[y + 1][x] + monun[y + 2][x]
def sv_4(x, y, monun):
    if len(monun[0]) <= x + 2:
        return 0
    if len(monun) <= y + 1:
        return 0
    return monun[y][x] + monun[y + 1][x] + monun[y + 1][x + 1] + monun[y + 1][x + 2]

n, m = map(int, input().split())
monun = [list(map(int, input().split())) for _ in range(n)]
hap = 0
for i_n in range(n):
    for i_m in range(m):
        if o_1(i_m, i_n, monun) > hap:
            hap = o_1(i_m, i_n, monun)
        if o_2(i_m, i_n, monun) > hap:
            hap = o_2(i_m, i_n, monun)
        if t_1(i_m, i_n, monun) > hap:
            hap = t_1(i_m, i_n, monun)
        if th_1(i_m, i_n, monun) > hap:
            hap = th_1(i_m, i_n, monun)
        if th_2(i_m, i_n, monun) > hap:
            hap = th_2(i_m, i_n, monun)
        if th_3(i_m, i_n, monun) > hap:
            hap = th_3(i_m, i_n, monun)
        if th_4(i_m, i_n, monun) > hap:
            hap = th_4(i_m, i_n, monun)
        if f_1(i_m, i_n, monun) > hap:
            hap = f_1(i_m, i_n, monun)
        if f_2(i_m, i_n, monun) > hap:
            hap = f_2(i_m, i_n, monun)
        if f_3(i_m, i_n, monun) > hap:
            hap = f_3(i_m, i_n, monun)
        if f_4(i_m, i_n, monun) > hap:
            hap = f_4(i_m, i_n, monun)
        if s_1(i_m, i_n, monun) > hap:
            hap = s_1(i_m, i_n, monun)
        if s_2(i_m, i_n, monun) > hap:
            hap = s_2(i_m, i_n, monun)
        if s_3(i_m, i_n, monun) > hap:
            hap = s_3(i_m, i_n, monun)
        if s_4(i_m, i_n, monun) > hap:
            hap = s_4(i_m, i_n, monun)
        if sv_1(i_m, i_n, monun) > hap:
            hap = sv_1(i_m, i_n, monun)
        if sv_2(i_m, i_n, monun) > hap:
            hap = sv_2(i_m, i_n, monun)
        if sv_3(i_m, i_n, monun) > hap:
            hap = sv_3(i_m, i_n, monun)
        if sv_4(i_m, i_n, monun) > hap:
            hap = sv_4(i_m, i_n, monun)
print(hap)

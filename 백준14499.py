Dice = {
    #   2
    # 4 1 3
    #   5
    #   6

    # 주사위전개도의 행방향(4, 1, 3)의 정보를 담고 있는 배열 
    "row" : [0, 0, 0],
    # 주사위전개도의 열방향(2, 1, 5, 6)의 정보를 담고 있는 배열
    "column": [0, 0, 0, 0]
}

def reshape_Dice(direction):
    #            2        2
    # 동쪽으로: 4 1 3 -> 6 4 1
    #            5        5
    #            6        3
    if direction == 1:
        Dice["row"][0], Dice["row"][1], Dice["row"][2], Dice["column"][1], Dice["column"][3] = Dice["column"][3], Dice["row"][0], Dice["row"][1], Dice["row"][0], Dice["row"][2]
    #            2        2
    # 서쪽으로: 4 1 3 -> 1 3 6
    #            5        5
    #            6        4
    elif direction == 2:
        Dice["row"][0], Dice["row"][1], Dice["row"][2], Dice["column"][1], Dice["column"][3] = Dice["row"][1], Dice["row"][2], Dice["column"][3], Dice["row"][2], Dice["row"][0]

    #            2        1
    # 북쪽으로: 4 1 3 -> 4 5 3
    #            5        6
    #            6        2
    elif direction == 3:
        Dice["column"][0], Dice["column"][1], Dice["column"][2], Dice["column"][3], Dice["row"][1] = Dice["column"][1], Dice["column"][2], Dice["column"][3], Dice["column"][0], Dice["column"][2]

    #            2        6
    # 북쪽으로: 4 1 3 -> 4 2 3
    #            5        1
    #            6        5
    elif direction == 4:
        Dice["column"][0], Dice["column"][1], Dice["column"][2], Dice["column"][3], Dice["row"][1] = Dice["column"][3], Dice["column"][0], Dice["column"][1], Dice["column"][2], Dice["column"][0]


# 지도크기(N, M) 가로, 주사위의 현재좌표(x, y), 명령 개수
N, M, now_x, now_y, K = map(int, input().split())
# 지도 모양
Atlas = [list(map(int, input().split())) for _ in range(N)]
# 명령 리스트
to_do = list(map(int, input().split()))

for i in range(K):
    check = False
    do_it = to_do[i]
    if do_it == 1 and now_y < M-1:
        now_y += 1
        check = True
    elif do_it == 2 and now_y > 0: 
        now_y -= 1
        check = True
    elif do_it == 3 and now_x > 0:
        now_x -= 1
        check = True
    elif do_it == 4 and now_x < N-1:
        now_x += 1
        check = True
    if check:
        reshape_Dice(do_it)
        # 바닥면을 지도에 복사
        if Atlas[now_x][now_y] == 0:
            Atlas[now_x][now_y] = Dice["column"][3]
        # 지도를 바닥면에 복사
        else:
            Dice["column"][3] = Atlas[now_x][now_y]
            Atlas[now_x][now_y] = 0
        print(Dice["column"][1])
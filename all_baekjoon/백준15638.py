N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

direct = ((-1, 0), (0, 1), (1, 0), (0, -1))
CCTV = {1 : [[0], [1], [2], [3]],
        2 : [[0, 2], [1, 3]],
        3 : [[0, 1], [1, 2], [2, 3], [3, 0]],
        4 : [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        5 : [[0, 1, 2, 3]]}

CCTV_Point, CCTV_Case, WALL_Num = [], [], 0
from itertools import product
for i, j in product(range(N), range(M)):
  if 1 <= room[i][j] <= 5:
    CCTV_Case.append(CCTV[room[i][j]])
    CCTV_Point.append((i, j))
  elif room[i][j] == 6:
    WALL_Num += 1

# CCTV방향의 모든 경우의 수 계산
ALL_Case = list(product(*CCTV_Case))

answer = 100
# 각 Case당 사각지대의 최소 크기 계산
for Case in ALL_Case:
  CAN_SEE = [[False] * M for _ in range(N)]
  # 각 Case의 CCTV위치와 방향에 따라 CAN_SEE 설정
  for Point, dir in zip(CCTV_Point, Case):
    # 1. CCTV위치는 CAN_SEE
    CAN_SEE[Point[0]][Point[1]] = True
    # 2. CCTV위치에서부터 dir방향으로 CAN_SEE
    for d in dir:
      now_x, now_y = Point[0], Point[1]
      dx, dy = direct[d][0], direct[d][1]

      nxt_x, nxt_y = now_x + dx, now_y + dy
      while nxt_x >= 0 and nxt_y >= 0 and nxt_x < N and nxt_y < M and room[nxt_x][nxt_y] != 6:
        CAN_SEE[nxt_x][nxt_y] = True
        nxt_x += dx
        nxt_y += dy
  answer = min(answer, N * M - sum(map(sum, CAN_SEE)) - WALL_Num)
print(answer)
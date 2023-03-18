N, M, K = map(int, input().split())
Stickers = []
NoteBook = [[False] * M for _ in range(N)]
for _ in range(K):
  R, C = map(int, input().split())
  Sticker = [list(map(int, input().split())) for _ in range(R)]
  Stickers.append(Sticker)

# 위치를 찾아 스티커를 붙이고 스티커를 붙였는지 여부를 반환
from itertools import chain
def find_loc(Sticker, NoteBook):
  comp_Sticker = list(chain(*Sticker))
  for start_i in range(len(NoteBook) - len(Sticker) + 1):
    for start_j in range(len(NoteBook[0]) - len(Sticker[0]) + 1):
      s_i, e_i = start_i, start_i + len(Sticker)
      s_j, e_j = start_j, start_j + len(Sticker[0])
      slice_Note = [NoteBook[i][s_j:e_j] for i in range(s_i, e_i)]
      comp_NoteBook = list(chain(*slice_Note))
      if all([not(comp_Sticker[i] and comp_NoteBook[i]) for i in range(len(comp_NoteBook))]):
        for i in range(s_i, e_i):
          for j in range(s_j, e_j):
            if Sticker[i - s_i][j - s_j]:
              NoteBook[i][j] = True
        return True
  return False

# 스티커 회전을 담당하는 함수
def turn_Sticker(Sticker):
  turn = [[False] * len(Sticker) for _ in range(len(Sticker[0]))]
  for i in range(len(Sticker[0])):
    for j in range(len(Sticker)):
      turn[i][j] = Sticker[len(Sticker) - 1 - j][i]
  return turn

# 주어진 순서대로 답을 도출하는 함수
def attach(Stickers, NoteBook):
  for Sticker in Stickers:
    angle = 0
    while (not find_loc(Sticker, NoteBook)) and (angle < 360):
      Sticker = turn_Sticker(Sticker)
      angle += 90
  return sum(map(sum, NoteBook))

print(attach(Stickers, NoteBook))
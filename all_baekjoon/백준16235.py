# Map[i][j] = k              i,j에 존재하는 양분
# TreeInfo[i][j] = [a, b, c] i,j에 존재하는 나무의 나이
# food[i][j] = k             i,j에 추가할 양분의 양
from itertools import product

def Spring_And_Summer(Map, Tree_Info):
  for i, j in product(range(len(Map)), range(len(Map))):
    # 나이가 어린 순으로 양분을 먹는다.
    Tree_Info[i][j].sort()
    del_index = -1
    num = 0
    for k in range(len(Tree_Info[i][j])):
      # 양분을 먹지 못한 나무들은 모두 죽어 양분이 된다. 정렬되어 있음을 유의
      if Map[i][j] < Tree_Info[i][j][k]:
        num += int(Tree_Info[i][j][k] / 2)
        if del_index == -1:
          del_index = k
      # 양분을 먹은 나무들은 나이가 한살 증가한다.
      else:
        Map[i][j] -= Tree_Info[i][j][k]
        Tree_Info[i][j][k] += 1
    if del_index != -1:
      Map[i][j] += num
      del Tree_Info[i][j][del_index:]

def Autumn_And_Winter(Map, Tree_Info, food):
  num = 0
  for i, j in product(range(len(Map)), range(len(Map))):
    # 가을에는 나무가 번식한다.
    for k in range(len(Tree_Info[i][j])):
      if Tree_Info[i][j][k] % 5 == 0:
        if i-1>=0 and j-1>=0:             Tree_Info[i-1][j-1].append(1)
        if i-1>=0:                        Tree_Info[i-1][j].append(1)
        if i-1>=0 and j+1<len(Map):       Tree_Info[i-1][j+1].append(1)
        if j-1>=0:                        Tree_Info[i][j-1].append(1)
        if j+1<len(Map):                  Tree_Info[i][j+1].append(1)
        if i+1<len(Map) and j-1>=0:       Tree_Info[i+1][j-1].append(1)
        if i+1<len(Map):                  Tree_Info[i+1][j].append(1)
        if i+1<len(Map) and j+1<len(Map): Tree_Info[i+1][j+1].append(1)
    # 겨울에는 양분이 추가된다.
    Map[i][j] += food[i][j]

N, M, K = map(int, input().split())
Map = [[5]*N for _ in range(N)]
Tree_Info = [[[]*1 for _ in range(N)] for _ in range(N)]
food = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
  x, y, z = map(int, input().split())
  Tree_Info[x-1][y-1].append(z)

for _ in range(K):
  Spring_And_Summer(Map, Tree_Info)
  Autumn_And_Winter(Map, Tree_Info, food)

result = 0
for i, j in product(range(len(Map)), range(len(Map))):
  result += len(Tree_Info[i][j])
print(result)
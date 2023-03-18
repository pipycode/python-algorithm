# N: 세로선의 개수 (2 <= N <= 10)
# H: 가로선을 놓을 수 있는 점선의 수 (1 <= H <= 30)
# M: 이미 놓여있는 가로선의 수
N, M, H = map(int, input().split())

ladder = [[0]*N for _ in range(H)]
for _ in range(M):
  x, y = map(int, input().split())
  ladder[x-1][y-1] = 1             # x-1, y-1위치에서 오른쪽으로 이동해야 함
  ladder[x-1][y] = -1                # x, y위치에서는 왼쪽으로 이동해야 함

# 시뮬레이션 함수
def simulation(ladder):
  for i in range(N):   # i는 사다리 번호
    ptr = i
    for j in range(H): # j는 가로선 수
      ptr += ladder[j][ptr]
    if ptr != i:
      return False
  return True

from itertools import product
def manipulate(ladder, N, H):
  num = 4
  if simulation(ladder): return 0
  for i, j in product(range(H), range(N - 1)):
    if ladder[i][j] != 0 or ladder[i][j+1] != 0: continue
    ladder[i][j] = 1
    ladder[i][j+1] = -1
    if simulation(ladder): return min(num, 1)
    
    for m, n in product(range(i, H), range(N - 1)):
      if m == i and n <= j: continue
      if ladder[m][n] != 0 or ladder[m][n+1] != 0: continue
      ladder[m][n] = 1
      ladder[m][n+1] = -1
      if simulation(ladder): num = min(num, 2)

      for x, y in product(range(m, H), range(N - 1)):
        if x == m and y <= n: continue
        if ladder[x][y] != 0 or ladder[x][y+1] != 0: continue
        ladder[x][y] = 1
        ladder[x][y+1] = -1
        if simulation(ladder): num = min(num, 3)

        ladder[x][y] = 0
        ladder[x][y+1] = 0

      ladder[m][n] = 0
      ladder[m][n+1] = 0

    ladder[i][j] = 0
    ladder[i][j+1] = 0
  
  return -1 if num == 4 else num

print(manipulate(ladder, N, H))
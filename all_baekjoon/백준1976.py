N = int(input())
M = int(input())

city = []
for i in range(N):
  city.append(list(map(int, input().split())))

travel = list(map(int, input().split()))

# 여행경로 반복 가능 ( A B C -> A -> B -> A -> C )
# 1. 목적지와 출발지가 겹치면 합칠 수 있다.
#     - (A -> B) 가능, (B -> C) 가능 == (A -> B -> C) 가능
# 2. 출발지가 같으면 합칠 수 있다.
#     - (A -> B) 가능, (A -> C) 가능 == (A -> B -> C) 가능


# city[i][j]를 다시 설정하는 함수
# 즉, visited[i][j]는 i에서 j로 갈 수 있는지 알 수 있음
from collections import deque
def BFS(start, N, city, visited):
  q = deque([start])
  visited[start][start] = True
  while q:
    now = q.popleft()
    nxt = [j for j in range(len(city[now])) if city[now][j]]
    if nxt:
      for j in nxt:
        if not visited[start][j]:
          visited[start][j] = True
          q.append(j)
  
visited = [[False] * N for _ in range(N)]
for i in range(N):
  BFS(i, N, city, visited)

start = travel[0] - 1
for i in range(1, len(travel)):
  if visited[start][travel[i] - 1]:
    start = travel[i] - 1
  else:
    check = False
    for j in range(i - 1):
      if visited[travel[j] - 1][travel[i] - 1]:
        check = True
        start = travel[i] - 1
        break
    if not check:
      break

if start == (travel[len(travel) - 1] - 1):
  print("YES")
else:
  print("NO")
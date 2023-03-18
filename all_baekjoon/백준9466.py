import sys
sys.setrecursionlimit(111111)
# 최종적으로 현재 DFS재귀에서 팀에 속한 학생들의 수를 RETURN
def DFS(now, num, visited, number):
  number[now] = num
  nxt = pick[now]
  # 1. 중간의 학생이 자기 자신을 선택해 사이클이 끝난 경우
  if now == nxt:
    visited[now] = True
    number[now] = 0
    return 1
  # 2. 이전 DFS재귀에서 사이클 판별을 한 적이 있는 경우
  elif visited[nxt]:
    visited[now] = True
    number[now] = 0
    return 0
  # 3. 현재 DFS재귀에서 사이클이 발생한 경우
  elif number[nxt]:
    result = number[now] - number[nxt] + 1
    visited[now] = True
    number[now] = 0
    return result
  else:
    result = DFS(nxt, num + 1, visited, number)
    visited[now] = True
    number[now] = 0
    return result

T = int(input())
for _ in range(T):
  n = int(input())
  pick_list = list(map(int, input().split()))

  pick = [0] * (n + 1)
  for x, y in enumerate(pick_list):
    pick[x + 1] = y

  # visited는 이전에 진행했던 DFS에서 방문한 적이 있는 노드인지 확인
  # number는 현재 진행중인 DFS에서 방문순서를 확인
  visited = [False] * (n + 1)
  number = [0] * (n + 1)
  result = 0
  for i in range(1, n + 1):
    if not visited[i]:
      result += DFS(i, 1, visited, number)
  print(n - result)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
friends = [[] for _ in range(N + 1)]
for _ in range(N-1):
  x, y = map(int, input().split())
  friends[x].append(y)
  friends[y].append(x)

visited = [False] * (N + 1)
def dfs(now):
  visited[now] = True
  children = [i for i in friends[now] if not visited[i]]
  now_pick, now_not_pick = 1, 0
  if not children:
    return [now_pick, now_not_pick]
  else:
    for child in children:
      child_pick, child_not_pick = dfs(child)
      now_pick += min(child_pick, child_not_pick)
      now_not_pick += child_pick
    return [now_pick, now_not_pick]

print(min(dfs(1)))
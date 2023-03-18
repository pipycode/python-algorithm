N = int(input())
population = list(map(int, input().split()))
population.insert(0, 0)
city = [list(map(int, input().split())) for _ in range(N)]
city.insert(0, [])

from collections import deque
def bfs(start, visited):
    visited[start] = True
    q = deque([start])
    while q:
        now = q.popleft()
        for nxt in city[now][1:]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    

total_population = sum(population)
equality = 1e9
# 개수를 기준으로 나눌 수 있는 모든 경우 생각
from itertools import combinations
for choose in range(1, N//2+1):
    for first_area in combinations(range(1, N+1), choose):
        second_area = [area for area in range(1, N+1) if area not in first_area]
        # 1. 선거구를 나눈 방법이 가능한지 확인
        visited_first = [True] * (N+1)
        for area in first_area:
            visited_first[area] = False
            
        visited_second = [True] * (N+1)
        for area in second_area:
            visited_second[area] = False
            
        bfs(first_area[0], visited_first)
        bfs(second_area[0], visited_second)
        
        # 2. 가능할 경우 점수 update
        if all(visited_first) and all(visited_second):
            equality = min(equality, 
                        abs(total_population-(2*sum([population[area] for area in first_area]))))

if equality == 1e9:
    print(-1)
else:
    print(equality)
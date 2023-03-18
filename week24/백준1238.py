N, M, X = map(int, input().split())

city = [[] for _ in range(1001)] # city[i] = (j, cost)
for i in range(M):
    start, end, cost = map(int, input().split())
    city[start].append([cost, end])

# 참석 후 돌아갈 때 = dijkstra
from heapq import heappush, heappop
INF = 1e9
def dijkstra(start):
    result = [INF] * 1001
    heap = []
    result[start] = 0
    heappush(heap, [0, start])
    while heap:
        cost_now, now = heappop(heap)
        if result[now] < cost_now:
            continue
        for cost_nxt, nxt in city[now]:
            total_cost = cost_now + cost_nxt
            if total_cost < result[nxt]:
                result[nxt] = total_cost
                heappush(heap, [total_cost, nxt])
    return result

back = dijkstra(X)[1:N+1]
result = [dijkstra(i)[X] + back[i-1] for i in range(1, N+1)]
print(max(result))

############################################
import sys
from collections import defaultdict
import heapq       # 우선 순위 큐

def dijkstra(start, graph):  #  O(ELogE) 
    # X 로부터 오는 경로의 최소값
    dp = [int(1e9)] * (N + 1)  # 무한대로 초기화
    dp[start] = 0
    q = []
    heapq.heappush(q, (0, start))   # 거리 순으로 최소 힙 생성

    while q:   # O(N*ELogE)
        dist, cur = q.pop()   # 가장 짧은 거리의 노드를 (LogN의 시간에 꺼내기)
        if dist > dp[cur]:    # 이미 최단 비용이 정해진 노드라면 패스(방문 처리)
            continue

        for node_index, node_cost in graph[cur]:  # 가장 최단 거리 노드의 인접한 노드 검사
            new_cost = dist + node_cost

            if dp[node_index] > new_cost:  # 비용이 더 작다면 갱신
                dp[node_index] = new_cost
                q.append((new_cost, node_index))  # 거리 값이 갱신된 최단 거리 노드만 우선순위 큐에 추가
    return dp

input = sys.stdin.readline
N, M, X = map(int, input().split())
graph_origin = defaultdict(list)
result = 0

for _ in range(M):
    s, e, d = map(int, input().split())
    graph_origin[s].append((e, d))    # 정방향 그래프 : X -> 특정 노드
    
dist_down = dijkstra(X, graph_origin)
result = [dijkstra(i, graph_origin)[X] + dist_down[i] for i in range(1, N+1)]
print(max(result))
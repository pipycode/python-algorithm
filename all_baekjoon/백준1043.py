N, M = map(int, input().split())

truth = sum([pow(2, t-1)for t in list(map(int, input().split()))[1:]])
party = [sum([pow(2, t-1)for t in list(map(int, input().split()))[1:]]) for _ in range(M)]

for _ in range(M):
    for p in party:
        # 교집합이 존재할 경우
        if truth & p:
            truth = truth | p

result = 0
for p in party:
    # 위에서 최종적으로 집합을 만든 후 교집합이 존재하지 않는 party를 센다
    if not truth & p:
        result += 1
        
print(result)
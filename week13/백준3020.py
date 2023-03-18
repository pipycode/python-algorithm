# 누적합 풀이
N, H = map(int, input().split())

Obstacle = [0]*(H + 1)

# Obstacle은 1부터 시작, H가 마지막
# 시작점엔+1, 마지막점을 지나고 난 후엔-1    
# => 이 다음 for문에서 장애물의 위치를 한번에 계산할 수 있다.
for i in range(N):
  temp = int(input())
  if i % 2 == 0:
    Obstacle[1] += 1
    Obstacle[temp + 1] -= 1
  else:
    Obstacle[H - temp + 1] += 1

# 이 과정을 통해 장애물의 위치 한번에 계산 가능
for i in range(1, H):
  Obstacle[i + 1] += Obstacle[i]

result = min(Obstacle[1:])
print(result, Obstacle[1:].count(result))
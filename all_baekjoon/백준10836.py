# 100점/15점
import sys

M, N = map(int, input().split())

HOME = [[1] * M for _ in range(M)]
grow = [0] * (2*M-1)
for _ in range(N):
    zero, one, two = map(int, input().split())
    one += zero
    two += one
    for i in range(zero, one):
        grow[i] += 1
    for i in range(one, two):
        grow[i] += 2
    
point = [M-1, 0]
direction = ((-1, 0), (0, 1))
d = 0
# 가장자리 성장
for k in range(2*M-1):
    HOME[point[0]][point[1]] += grow[k]
    if k==M-1: d+=1
    point[0], point[1] = point[0]+direction[d][0], point[1]+direction[d][1]

# 안쪽 성장
for i in range(1, M):
    for j in range(1, M):
        HOME[i][j] += grow[M+j-1]


for i in range(M):
    for j in range(M):
        print(HOME[i][j], end=' ')
    print()

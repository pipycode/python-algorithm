n = int(input()) # 점 갯수
points = []
size = 0
for _ in range(n//2-1):
    sy,sx = map(int, input().split())
    ey,ex = map(int, input().split())
    points.append([sx,sy,ey-sy,0]) # sx:0부터 깊이 sy:시작점 ey-sy:바닥의 길이 0:빠진 물의 높이
    size += sx*(ey-sy) # 채워진 물의 양

m = int(input()) # 구멍 개수
holes = []
for _ in range(m):
    sy,sx,ey,ex = map(int, input().split())
    holes.append([sx,sy,ex,ey]) # 구멍이 있는 바닥

holes.sort(key=lambda x:x[1])

def solv():
    global size
    hole_idx = 0
    for idx in range(n//2-1):
        x, y, length, water = points[idx]
        if hole_idx < m and holes[hole_idx][0] == x and holes[hole_idx][1] == y: # 만약 구멍이 있는 선분일 경우
            hole_idx += 1
            renew_water(idx,-1,x,-1) # 현재 점 기준 왼쪽
            renew_water(idx+1, n//2, x,1) # 현재 점 기준 오른쪽

    for idx in range(n//2-1):
        size -= points[idx][3]*points[idx][2] # 바닥의 길이과 빼낸 물높이의 곱 = 빠진 물의 양
    print(size)

def renew_water(start,end,h,op):
    global points

    for idx in range(start,end,op):
        if idx >= len(points):
            return
        if points[idx][3] < h: # 빼낸 물의 양이 현재 깊이보다 작을 때 (물을 더 뺄 수 있을 때)
            if points[idx][0] < h: # 만약 해당 점의 높이가 구멍보다 작다면
                h = points[idx][0] # 기준을 해당 점으로 바꿈
            points[idx][3] = h # 빼낸 물의 양
        else:
            break

solv()
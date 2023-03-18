r1, c1, r2, c2 = map(int, input().split())

Print_Matrix = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
direction = 0

now_r, now_c = 0, 0
width = 0
number = 1
while not all(map(all, Print_Matrix)):
    # 한 변의 길이: 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, ...
    width += 1
    for _ in range(2):
        for _ in range(width):
            if r1 <= now_r <= r2 and c1 <= now_c <= c2:
                Print_Matrix[now_r - r1][now_c - c1] = number
            number += 1
            now_r += dx[direction]
            now_c += dy[direction]
        direction = (direction + 1) % 4

max_number_len = len(str(max(map(max, Print_Matrix))))
for i in range(r2 - r1 + 1):
    for j in range(c2-c1+1):
        print(str(Print_Matrix[i][j]).rjust(max_number_len), end=" ")
    print()
H, W = map(int, input().split())
Ground_list = list(map(int, input().split()))
# 0은 빈공간, 1은 땅, 2는 물
Ground = [[2] * W for _ in range(H)]
for i, h in enumerate(Ground_list):
    for j in range(h):
        Ground[H-j-1][i] = 1

for i in range(len(Ground)):
    # 왼쪽이 비어있으면 물이 빠짐
    if Ground[i][0] == 2:
        j = 0
        while j<W and Ground[i][j]==2:
            Ground[i][j] = 0
            j += 1
    # 오른쪽이 비어있으면 물이 빠짐
    if Ground[i][W-1] == 2:
        j = W-1
        while j>=0 and Ground[i][j]==2:
            Ground[i][j] = 0
            j -= 1
 
print(sum([Ground[i].count(2) for i in range(H)]))
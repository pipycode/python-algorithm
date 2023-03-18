# 한 가장자리를 회전하는 함수
def rotate_one(arr, r, c, s):
    direction = [[0, 1], [1, 0], [0,-1], [-1,0]]
    i, j = r-s, c-s+1
    # 원래 자리로 돌아올 때 까지
    pre = arr[i][j-1]
    d = 0
    while not(i==(r-s) and j==(c-s)):
        temp=arr[i][j]
        arr[i][j]=pre
        pre=temp
        if not (r-s<=i+direction[d][0]<=r+s and c-s<=j+direction[d][1]<=c+s):
            d=(d+1)%4
        i,j=i+direction[d][0],j+direction[d][1]
    arr[i][j] = pre

def rotate_all(arr, r, c, s):
    while s>0:
        rotate_one(arr, r, c, s)
        s-=1

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cal_info = [list(map(int, input().split())) for _ in range(K)]
result = 5001
from itertools import permutations
for order in permutations(range(K), K):
    arr_test = [arr[i][:] for i in range(N)]
    for i in order:
        r, c, s = cal_info[i]
        rotate_all(arr_test, r-1, c-1, s)
    result = min(result, min([sum(arr_test[i]) for i in range(N)]))

print(result)
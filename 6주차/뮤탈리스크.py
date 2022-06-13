import itertools

n = int(input()) # scv 개수
lst = list(map(int, input().split())) # scv 체력

dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)] # 탐색을 위한 3차원 리스트 생성

def go(a, b, c):
    if a < 0:
        return go(0, b, c) # a의 값이 0보다 작으면 a를 0으로 생각하고 재귀 
    if b < 0:
        return go(a, 0, c) # b의 값이 0보다 작으면 a를 0으로 생각하고 재귀
    if c < 0:
        return go(a, b, 0) # c의 값이 0보다 작으면 a를 0으로 생각하고 재귀
    if a == 0 and b == 0 and c == 0: # 재귀 하다가 결국 모두 다 0이면 0 리턴
        return 0
    if dp[a][b][c] != -1: # 초기값은 모두 -1이지만 변했다면 그 값을 리턴
        return dp[a][b][c]
    dp[a][b][c] = 999999999 # 아니면 999999999로 설정
    for case in list(itertools.permutations([1, 3, 9])): # permutation으로 조합한 공격하는 리스트를 담은 case
        dp[a][b][c] = min(dp[a][b][c], go(a - case[0], b - case[1], c - case[2])) # 그 케이스로 하나하나 빼서 최소값을 저장한다.
    dp[a][b][c] += 1 # 초기 값을 -1로 했기 때문에 1을 더해준다.
    return dp[a][b][c] # 최소값 리턴

scv = [0, 0, 0] # 초기 scv 세팅 값
for i in range(len(lst)): # scv에 실제 체력 값 넣기
    scv[i] = lst[i]
print(go(scv[0], scv[1], scv[2])) # go 함수 실행

# DP
# DP[i][j]는 i,j가 왼쪽아래 모서리인 정사각형의 최대 넓이
# DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
def solution(board):
    DP = [[0]*len(board[0]) for _ in range(len(board))]
    
    # 초기화
    for i in range(len(board)):
        if board[i][0]:
            DP[i][0] = 1
    for j in range(len(board[0])):
        if board[0][j]:
            DP[0][j] = 1
    # DP적용
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1

    return pow(max([max(DP[i]) for i in range(len(DP))]), 2)
# 백준 1915
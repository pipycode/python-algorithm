def solution(triangle):
    intList = triangle
    SUM = [[0] * len(i) for i in intList] # 합계 적는 리스트
    width = height = 0
    for i in intList:
        for j in i:
            if height == 0 and width == 0: # 가장 처음 합
                SUM[height][width] = j # 윗줄이 없어서 더할 값이 없기 때문에 자기 자신 저장
            elif width == 0: # 만약 맨 왼쪽이라면
                SUM[height][width] = SUM[height-1][width] + j # 그 윗줄의 가장 왼쪽 값 가져와서 자기 자신과의 합 저장
            elif width == (len(i)-1): # 만약 맨 오른쪽이라면
                SUM[height][width] = SUM[height-1][width-1] + j # 그 윗줄의 가장 오른쪽 값 가져와서 자기 자신과의 합 저장
            else: # 그외 나머지
                SUM[height][width] = max(SUM[height-1][width] + j, SUM[height-1][width-1] + j) # 좌우 경로에 따른 값 중 큰 값 저장
            width +=1
        height   +=1
        width = 0 # 너비 초기화

    return max(map(max,SUM))

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
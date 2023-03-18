def can_attach(Base_Paper, Point, Attach_Paper_Size):
    '''
    Base_Paper:         10x10의 종이
    Point:              i, j (붙이고 싶은 종이의 좌측 상단 점)
    Attach_Paper_Size:  10x10종이에 붙일 색종이의 크기
    return:             주어진 조건에 따라 붙일 수 있으면 True
    '''
    if Point[0] + Attach_Paper_Size > 10 or Point[1] + Attach_Paper_Size > 10:
        return False
    if all([all(Base_Paper[Point[0] + i][Point[1] : Point[1] + Attach_Paper_Size]) for i in range(Attach_Paper_Size)]):
        return True
    else:
        return False
    
def attach(Base_Paper, Point, Attach_Paper_Size):
    '''
    Base_Paper:         10x10의 종이
    Point:              i, j (붙이고 싶은 종이의 좌측 상단 점)
    Attach_Paper_Size:  10x10종이에 붙일 색종이의 크기
    __call__:           Base_Paper의 주어진 위치에 색종이를 붙임
    '''
    for i in range(Point[0], Point[0] + Attach_Paper_Size):
        for j in range(Point[1], Point[1] + Attach_Paper_Size):
            Base_Paper[i][j] = 0

def detach(Base_Paper, Point, Detach_Paper_Size):
    '''
    Base_Paper:         10x10의 종이
    Point:              i, j (붙이고 싶은 종이의 좌측 상단 점)
    Attach_Paper_Size:  10x10종이에 붙일 색종이의 크기
    __call__:           Attach한 색종이를 도로 땜
    '''
    for i in range(Point[0], Point[0] + Detach_Paper_Size):
        for j in range(Point[1], Point[1] + Detach_Paper_Size):
            Base_Paper[i][j] = 1
            
def find_one(Base_Paper):
    '''
    Base_Paper:         10x10의 종이
    return:             1이 적혀있는 곳의 위치(만약 한군데도 없으면 -1, -1)
    '''
    for i in range(10):
        for j in range(10):
            if Base_Paper[i][j]:
                return i, j
    return -1, -1

def DFS(Base_Paper, Color_Paper):
    '''
    Base_Paper:         10x10의 종이
    Color_Paper:        1x1, 2x2, ... 5x5 색종이 중 붙인 색종이의 개수
    return:             필요한 색종이의 개수
    '''
    result = 999
    i, j = find_one(Base_Paper)
    if (i==-1 and j==-1):
        return sum(Color_Paper)
    elif sum(Color_Paper) >= result:
        return result
    else:
        Color_Paper_Size = 5
        while Color_Paper_Size>0:
            # 해당 크기의 색종이의 개수가 5개를 넘어가면 붙일 수 없다.
            if Color_Paper[Color_Paper_Size] >= 5:
                Color_Paper_Size -= 1
                continue
            # 색종이를 붙일 수 있는 경우
            # 색종이를 붙인다 -> 붙인 상태에서 다음 상태들을 검사한다 -> 땐다
            if can_attach(Base_Paper, (i, j), Color_Paper_Size):
                attach(Base_Paper, (i, j), Color_Paper_Size)
                Color_Paper[Color_Paper_Size] += 1
                result = min(result, DFS(Base_Paper, Color_Paper))
                Color_Paper[Color_Paper_Size] -= 1
                detach(Base_Paper, (i, j), Color_Paper_Size)
            Color_Paper_Size -= 1
        # 만약 while문을 검사할 동안 i==-1, j==-1을 찾지 못하면 모두 덮는것이 불가능함
        return result

Base_Paper = [list(map(int, input().split())) for _ in range(10)]
Color_Paper = [0] * 6
result = DFS(Base_Paper, Color_Paper)
print(result if result != 999 else -1)
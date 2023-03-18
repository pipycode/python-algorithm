# yellow = r-2 * c-2
# brown = 2(r+c) - 4
def solution(brown, yellow):
    start = brown // 2
    for i in range(start, 0, -1): 
        row = i
        column = ((brown + 4) // 2) - row
        if (row-2) * (column-2) == yellow:
            return [i, column]
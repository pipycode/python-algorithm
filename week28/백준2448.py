def capture(arr:list, left_high, right_bottom):
    x_l, y_l = left_high
    x_r, y_r = right_bottom
    return [arr[i][y_l:y_r+1] for i in range(x_l, x_r+1)]

def paste(arr:list, capture, left_high, right_bottom):
    x_l, y_l = left_high
    x_r, y_r = right_bottom
    for i in range(x_l, x_r+1):
        for j in range(y_l, y_r+1):
            arr[i][j]=capture[i-x_l][j-y_l]
            
# 0~H까지의 ARR을 복사해 H+1에 붙여 넣는다
def capture_paste(arr, H):
    left_high = [0]
    for j in range(len(arr[0])):
        if arr[H - 1][j] == '*':
            left_high.append(j)
            break
        
    right_bottom = [H - 1]
    for j in range(len(arr[0])-1, 0, -1):
        if arr[H - 1][j] == '*':
            right_bottom.append(j)
            break
    captured_arr = capture(arr, left_high, right_bottom)
    
    W = right_bottom[1] - left_high[1] + 1
    middle = (right_bottom[1] + left_high[1]) // 2
    paste_left = [
        [right_bottom[0]+1, middle - W],
        [right_bottom[0]+H, middle - 1]
    ]
    paste_right = [
        [right_bottom[0]+1, middle + 1],
        [right_bottom[0]+H, middle + W]
    ]
    paste(arr, captured_arr, paste_left[0], paste_left[1])
    paste(arr, captured_arr, paste_right[0], paste_right[1])

def one_triangle(arr:list, H, W):
    arr[H][W] = '*'
    arr[H+1][W-1], arr[H+1][W+1] = '*', '*'
    arr[H+2][W-2], arr[H+2][W-1], arr[H+2][W], arr[2][W+1], arr[2][W+2] = '*', '*', '*', '*', '*'

import math
def main():
    N = int(input())
    h = N
    w = ((N // 3) * 5)+((N // 3)-1)
    arr = [[' ']*w for _ in range(N)]
    one_triangle(arr, 0, w//2)
    
    for i in range(int(math.log2(N // 3))):
        capture_paste(arr, 3 * pow(2, i))

    for i in range(N):
        print(''.join(arr[i]))

if __name__ == '__main__':
    main()
'''
N -> 최대 및변 크기
3=3*1 -> 5*1 + 0
6=3*2 -> 5*2 + 1
12=3*4 -> 5*4 + 3
24=3*8 -> 5*8 + 7
48=3*16 -> 5*16 + 15

N -> 높이
3=3*1 -> 1
6=3*2 -> 2
12=3*4 -> 4
24=3*8 -> 8
'''

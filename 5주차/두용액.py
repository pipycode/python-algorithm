N = int(input())
T = list(map(int, input().split()))
T.sort()
SUM = 1000000000
start = 0
end = N-1
A = B = 0

while start < end:
    now = T[start] + T[end]
    if abs(now) < SUM:
        SUM = now
        A = T[start]
        B = T[end]
    if now > 0:
        end = end - 1
    elif now < 0 :
        start = start + 1
    else:
        SUM = now
        A = T[start]
        B = T[end]
        break
print(A,B)

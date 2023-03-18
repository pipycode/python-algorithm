N = int(input())
U = sorted([int(input()) for _ in range(N)])

# x+y+z=k(3중for문) -> x+y=k-z(2중for문)
# check: 2개를 더했을 때, 가능한 수의 목록
check = set()
for x in range(len(U)):
    for y in range(x, len(U)):
        check.add(U[x]+U[y])

for k in range(len(U)-1, -1, -1):
    for z in range(k):
        if U[k]-U[z] in check:
            print(U[k])
            exit()
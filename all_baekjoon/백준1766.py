N, M = map(int, input().split())

info = [[0] for _ in range(32001)]
for _ in range(M):
    A, B = map(int, input().split())
    info[A].append(B)
    info[B][0] += 1

# start할 노드 중 쉬운 문제 먼저 solved에 넣는다.
solved = []
solve = [i for i in range(1, N+1) if not info[i][0]]
while len(solved) < N:
    problem = min(solve)
    solved.append(problem)
    solve.remove(problem)
    for nxt in info[solved[-1]][1:]:
        info[nxt][0] -= 1
        if not info[nxt][0]:
            solve.append(nxt)
print(' '.join(map(str, solved)))
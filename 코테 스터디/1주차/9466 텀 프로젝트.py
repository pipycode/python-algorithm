import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000000)

def dfs(i):
    global result
    
    cycle.append(i)
    visited[i] = True
    
    if visited[students[i]]:
        if students[i] in cycle:
            
            # 팀을 구한 학생의 수를 result에 더한다.
            result += len(cycle[cycle.index(students[i]):])
            return
    
    else:
        dfs(students[i])
            

T = int(input())

for _ in range(T):
    n = int(input())
    result = 0
    
    students = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
            
    # 전체 학생 수 - 팀을 구한 학생 수 = 팀에 속하지 못한 학생 수(답)
    print(n - result)
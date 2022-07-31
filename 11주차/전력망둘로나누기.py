def solution(n, wires):
    answer = 100
    
    for i in range(len(wires)):
        group_a = set()
        group_b = set()
        
        group_a.add(wires[i][0])
        group_b.add(wires[i][1])
        
        new_wires = wires[:i] + wires[i+1:]
        visited = [False] * (n-2)
        cur = 0

        while False in visited:
            if visited[cur] is False:
                if new_wires[cur][0] in group_a:
                    group_a.add(new_wires[cur][1])
                    visited[cur] = True
                elif new_wires[cur][0] in group_b:
                    group_b.add(new_wires[cur][1])
                    visited[cur] = True
                elif new_wires[cur][1] in group_a:
                    group_a.add(new_wires[cur][0])
                    visited[cur] = True
                elif new_wires[cur][1] in group_b:
                    group_b.add(new_wires[cur][0])
                    visited[cur] = True
                
            if cur == n-3:
                cur = 0
            else:
                cur += 1
            
        diff = abs(len(group_a) - len(group_b))
        if diff < answer:
            answer = diff
        
    if answer == 101:
        answer = 0
        
    return answer
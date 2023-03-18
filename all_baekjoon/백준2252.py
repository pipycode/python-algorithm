N, M = map(int, input().split())
students = {str(i+1):{'to':[], 'from':0} for i in range(N)}
for _ in range(M):
    A, B = input().split()
    students[A]['to'].append(B)
    students[B]['from'] += 1

from collections import deque
q = deque()
result  = []
for id in students:
    if not students[id]['from']:
        q.append(id)

while q:
    id = q.popleft()
    result.append(id)
    for nxt_id in students[id]['to']:
        students[nxt_id]['from'] -= 1
        if not students[nxt_id]['from']:
            q.append(nxt_id)

print(' '.join(result))
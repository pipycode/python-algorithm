def comp(A, B):
    swap = 0
    for a, b in zip(A, B):
        if a != b:
            swap += 1
    if swap == 1:
        return True
    else:
        return False

from collections import deque
def bfs(begin, target, words):
    num = 0
    visited = {word:False for word in words}
    q = deque([begin])
    while q:
        num += 1
        s = len(q)
        for _ in range(s):
            now = q.popleft()
            for word in words:
                if (not visited[word] and comp(now, word)):
                    if word == target:
                        return num
                    else:
                        visited[word] = True
                        q.append(word)
    return 0
            
def solution(begin, target, words):
    return bfs(begin, target, words)
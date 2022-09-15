from collections import deque
def bfs(_begin, _target, _words, visited, how):
    que = deque()
    for idx, word in enumerate(_words):
        diff = 0
        for i in range(len(_begin)):
            if word[i] != _begin[i]:
                diff += 1
            if diff >= 2:
                break
        if diff == 1:
            visited[idx] = True
            que.append(word)
            how[idx] = 1
    while que:
        now = que.popleft()
        if now == _target:
            return how[_words.index(now)]
        for idx, word in enumerate(_words):
            if visited[idx] == True:
                continue
            diff = 0
            for i in range(len(now)):
                if word[i] != now[i]:
                    diff += 1
                if diff >= 2:
                    break
            if diff == 1:
                visited[idx] = True
                que.append(word)
                how[idx] = how[_words.index(now)] + 1
    return 0
    
def solution(begin, target, words):
    visited = [False] * len(words)
    how = [0] * len(words)
    answer = bfs(begin, target, words, visited, how)
    return answer

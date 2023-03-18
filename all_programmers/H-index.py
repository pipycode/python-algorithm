def solution(citations):
    answer = 0
    citations.sort(key = lambda x:-x)
    for i, citation in enumerate(citations):
        if i + 1 <= citation:
            answer = i + 1
    return answer

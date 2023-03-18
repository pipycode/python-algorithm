from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for i in range(1, len(dungeons) + 1):
        for test in permutations(dungeons, i):
            HP = k
            check = True
            for visit in test:
                if HP >= visit[0]:
                    HP -= visit[1]
                else:
                    check = False
                    break
            if check:
                answer = i
    return answer
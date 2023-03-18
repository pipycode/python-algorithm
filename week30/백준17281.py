N = int(input())
sim_result = [list(map(int, input().split())) for _ in range(N)]

maximum_score = 0
number = [2, 3, 4, 5, 6, 7, 8, 9]
from itertools import permutations
for p in permutations(number, 8):
    order = list(p)
    order.insert(3, 1)
    
    num = 0
    score = 0
    for inning in sim_result:
        out = 0
        one, two, three = False, False, False
        while out < 3:
            if inning[order[num]-1] == 0:
                out += 1
            elif inning[order[num]-1] == 1:
                if three: score += 1
                one, two, three = True, one, two
                
            elif inning[order[num]-1] == 2:
                if two: score += 1
                if three: score += 1
                one, two, three = False, True, one
                
            elif inning[order[num]-1] == 3:
                if one: score += 1
                if two: score += 1
                if three: score += 1
                one, two, three = False, False, True
                
            elif inning[order[num]-1] == 4:
                score += 1
                if one: score += 1
                if two: score += 1
                if three: score += 1
                one, two, three = False, False, False
            
            num += 1
            num %= 9
    maximum_score = max(maximum_score, score)
print(maximum_score)
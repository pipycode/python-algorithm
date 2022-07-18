from itertools import combinations

L,C = map(int,input().split())
vowel = set('aeiou')
alpha = input().split()
alpha.sort()
answer = list(combinations(alpha, L)) # 오름차순으로 중복없는 조합
for combi in answer:
    ans = set(combi) - vowel # 차집합 = 만들어진 단어에서 모음을 제거한 경우
    if len(ans) >= 2 and len(set(combi) & vowel) >=1 : # 최소 2개의 자음으로 구성되고 최소 1개의 모음으로 구성
        print(''.join(combi))
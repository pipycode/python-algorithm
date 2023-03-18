from collections import Counter
def solution(id_list, report, k):
    answer = []
    dct = {}
    meil = Counter()
    for repo in set(report):
        ing, ed = repo.split()
        if ed in dct:
            dct[ed].append(ing)
        else:
            dct[ed] = [ing]
    
    for repo in dct:
        if len(dct[repo]) >= k:
            for ing in dct[repo]:
                meil[ing] += 1
                
    for ID in id_list:
        answer.append(meil[ID])
    return answer
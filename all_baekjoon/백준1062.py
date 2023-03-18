N, K = map(int, input().split())
words = [set(list(input())) for _ in range(N)]\
    
def convert_num(word:set):
    return sum(map(lambda x:pow(2, ord(x)-97), word))

def can_read(word, study):
    # word - study==0 이면 word를 읽을 수 있음
    if (word & ~study)==0: return True
    else: return False

if K<5:
    print(0)
else:
    words = list(map(convert_num, words))
    base = convert_num(('a', 'n', 't', 'i', 'c'))
    # antic는 꼭 가르쳐야 함
    not_study = [chr(i) for i in range(97, 97+26) if chr(i) not in ('a', 'n', 't', 'i', 'c')]

    from itertools import combinations
    result = 0
    for study in combinations(not_study, K - 5):
        study = convert_num(study) + base
        readable_list = list(filter(lambda word:can_read(word, study), words))
        if result < len(readable_list):
            result = len(readable_list)
    print(result)
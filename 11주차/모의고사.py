def solution(answers):
    supoza = ['12345','21232425','3311224455']
    index_supo = [0 for i in range(3)]
    collect_supo = {i:0 for i in range(1,4)}
    for answer in answers:
        for supo in range(3):
            if answer == int(supoza[supo][index_supo[supo]]):
                collect_supo[supo+1] += 1
            if index_supo[supo] == len(supoza[supo])-1:
                index_supo[supo] = 0
            else:
                index_supo[supo] += 1
    sorted_supo = dict(sorted(collect_supo.items(), key= lambda item : item[1],reverse=True))
    sorted_value = list(sorted_supo.values())
    sorted_key = list(sorted_supo.keys())
    for supo in range(2):
        if sorted_value[supo] != sorted_value[supo+1]:
            return sorted_key[:supo+1]
    if sorted_value[0] == sorted_value[1] == sorted_value[2]:
        return sorted_key[:3]
                
print(solution([1,3,2,4,2]))
print(solution([1,2,3,4,5]))
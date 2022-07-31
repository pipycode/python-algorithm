def solution(s):
    short = ''
    shortest = len(s)
    count = 0
    for slice_num in range(1,len(s)//2+1): # 몇 개 단위로 자를 것인가?
        for word_num in range(0,len(s), slice_num): # 잘랐을 때 같은지 비교하기
            if s[word_num:word_num+slice_num] == s[word_num+slice_num:word_num+slice_num+slice_num]: # 일정 길이만큼 다음 길이와 같다면
                count += 1
            else:
                if count == 0: # 하나도 같지 않다면
                    short = short + s[word_num:word_num+slice_num] # 그대로 새로운 문자열에 붙이기
                    count = 0
                else: # 같은 것이 있었지만 이제는 다르다면
                    short = short + str(count+1) + s[word_num:word_num+slice_num] # 개수를 포함해서 문자열에 붙이기
                    count = 0
        if shortest > len(short): # 만약 지금 나온 문자열이 이전보다 짧다면
            shortest = len(short)
        short = ''
        count = 0
    return shortest

# solution("aabbaccc")
# solution("ababcdcdababcdcd")
solution("abcabcdede")
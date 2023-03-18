# 단위의 총 경우의 수 = 500
# 입출력예의 설명 -> Brute Force
def solution(s):
    answer = 1000
    # 문자열을 i단위로 나누었을 때
    for i in range(1, int(len(s)/2) + 1):
        # 문자열을 단위별로 나눠 temp에 담아주는 함수
        temp = [ s[j*i : (j+1)*i] for j in range(int(len(s)/i))]
        if (len(s) % i) != 0:
            temp.append(s[int(len(s)/i)*i :])
        # temp를 검사하며 압축후 길이를 계산하는 함수
        num = 0
        check = 1
        # 길이 계산 후 더하기
        for j in range(1, len(temp)):
            if temp[j] == temp[j-1]:
                check += 1
            else:
                if check > 1:
                    num += len(str(check))
                num += len(temp[j-1])
                check = 1
        # 마지막 뒷처리
        if check > 1:
            num += len(str(check))
        num += len(temp[len(temp)-1])
        
        # 결과값 갱신
        if num < answer:
            answer = num
    # len(s) == 1인 경우
    if len(s) == 1:
        answer = 1
    return answer
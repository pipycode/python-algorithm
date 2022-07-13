def solution(phone_book):
    phone_book.sort() # 접두어가 되기 위해선 길이가 짧거나 같아야하므로 정렬
    for i in range(0,len(phone_book)-1): # 자기 자신과 그 다음을 계속 비교함
        # 문자열을 정렬했기 때문에, 다음 요소는 자신을 포함하거나 안하거나 둘 중 하나.. 
        # 그래서 자신의 길이만큼만 비교하면 됨
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]: # 그러다가 자신의 길이만큼 다른 요소가 같다면 접두어라고 판단
            return False
    return True
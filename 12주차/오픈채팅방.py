def solution(record):
    user_dict = dict()
    # user_dict = {
    #     사용자_ID(str) : 닉네임(str)
    # }
    answer = []
    for rec in record:
        word = rec.split()
        if len(word) == 3:
            user_dict[word[1]] = word[2]

    for rec in record:
        word = rec.split()
        if word[0] == 'Enter':
            answer.append(user_dict[word[1]]+'님이 들어왔습니다.')
        elif word[0] == 'Leave':
            answer.append(user_dict[word[1]]+'님이 나갔습니다.') # 출입 기록
        

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
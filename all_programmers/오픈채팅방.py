# 1 <= record <= 100000
def solution(record):
    answer = []
    user_info = {}
    # userID와 해당 user의 이름 각각 저장
    for data in record:
        info = list(data.split())
        if info[0] == "Enter" or info[0] == "Change":
            user_info[info[1]] = info[2]

    # 출력결과 계산
    for data in record:
        info = list(data.split())
        if info[0] == "Enter":
            answer.append(user_info[info[1]] + "님이 들어왔습니다.")
        elif info[0] == "Leave":
            answer.append(user_info[info[1]] + "님이 나갔습니다.")
    return answer
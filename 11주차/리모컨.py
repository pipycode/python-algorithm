# from itertools import product # 중복순열
# N = int(input())
# M = int(input())
# NOW = 100 # 기본 채널값
# if M != 0: # 만약 모두 멀쩡한 버튼이라면
#     err_buttons = input().split()
# elif M == 10: # 모든 버튼이 망가졌다면
#     print(abs(N-NOW))
#     exit()
# else:
#     err_buttons = ''

# buttons = list(set([str(i) for i in range(10)]) - set(err_buttons)) # 정상적인 버튼
# abs_num = 500000
# numbers = sorted(list(product(buttons, repeat = len(str(N))))) # 정상적인 버튼으로 누른 모든 채널
# press_count = 0 # 누른 횟수
# for num in numbers:
#     num = int(''.join(num))
#     if abs_num > abs(N-num): # 이전보다 목표한 채널에 가깝다면
#         if num == N: # 만약 순열 값이 목표한 채널이라면
#             press_count = len(str(num)) # 채널번호의 길이만큼만 누름
#         else:
#             abs_num = abs(N-num) # 해당 채널에서 목표한 채널로 가기 위해 눌러야하는 횟수
#             press_count = len(str(num)) + abs_num # 채널번호 길이만큼 누른 횟수 + 추가로 +/-를 누른 횟수

# if press_count-abs(N-NOW)>0: # 그냥 +/-로만 갔을 때 더 가깝다면
#     print(abs(N-NOW))
# else:
#     print(press_count)

N = int(input())  # 채널번호
M = int(input())  # 고장난 버튼의 개수
remote = {str(x) for x in range(10)}  # 리모컨버튼

if M != 0:
    remote -= set(input().split())  # 사용가능한 버튼 뽑아냄

min_cnt = abs(100-N)  # 일단 100과의 갭을 최소로 두고 계산

for k in range(1000000):
    num = str(k)
    for i in range(len(num)):
        if num[i] not in remote:  # 0~999999까지의 숫자 순회하면서 리모컨 버튼에 없으면 패쓰
            break
        if i == len(num)-1:  # 마지막 자리수까지 확인했으면 최소 카운팅 갱신
            min_cnt = min(min_cnt, abs(N-k)+len(num))

print(min_cnt)
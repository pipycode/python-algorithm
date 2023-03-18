# Idea
# 1. 꽉차면 적게 남은 것을 뺀다 -> 실패
# 2. 꽉차면 꼽았던 것 중 다시 꽂아야 하는 순서가 가장 뒤에 있는 것을 뽑는다.

from collections import Counter
N, K = map(int, input().split())

def nxt_dist_fc(l, d):
    for i in range(len(l)):
        if l[i] == d: return i
    return 999

# list를 정제한다
# ex. 1 2 3 3 3 3 -> 1 2 3
_device_list = list(map(int, input().split()))
device_list = [_device_list[0]]
for i in range(1, len(_device_list)):
    if _device_list[i] != device_list[-1]:
        device_list.append(_device_list[i])

# 정보들을 표현할 저장공간 정의
power_strip = [False] * 101
result = 0
for i, device in enumerate(device_list):
    # 현재 사용하려는 전기용품이 꽂혀있을 경우
    if power_strip[device]:
        continue
    # 멀티탭에 공간이 남아있는 경우
    elif N:
        power_strip[device] = True
        N -= 1
    # 멀티탭에 공간이 없는 경우 꽂혀있는 기기 중 다음 사용이 가장 많이 남은 기기를 제거
    else:
        now_power = [idx for idx, use in enumerate(power_strip) if use]
        remove = max(now_power, key= lambda idx:nxt_dist_fc(device_list[i+1:], idx))
        power_strip[remove] = False
        power_strip[device] = True
        result += 1
print(result)
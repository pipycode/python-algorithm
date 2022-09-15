n = int(input())
nums = list(map(int, input().split()))
if n == 1:
    print('A')
else:
    answer_list = []
    for a in range(-1001, 1002):
        b = nums[1] - nums[0] * a
        not_ok = False
        for i in range(1, n):
            if nums[i] != nums[i - 1] * a + b:
                not_ok = True
                break
        if not not_ok:
            answer_list.append(nums[n - 1] * a + b)
    answer_list = list(set(answer_list))
    if len(answer_list) == 0:
        print('B')
    elif len(answer_list) == 1:
        print(answer_list[0])
    else:
        print('A')

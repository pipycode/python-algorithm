N, M = map(int, input().split())
times = []
for _ in range(N):
    times.append(int(input()))

left = 0
answer = right = max(times) * M

while left <= right:
    mid = (left+right) // 2
    people = 0
    print(left, right)
    for time in times:
        people += mid//time

    if people < M:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(answer, mid)

print(answer)
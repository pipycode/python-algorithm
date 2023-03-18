# 데이터 전처리
start = 100
end = int(input())
M = int(input())
broken = []
if M != 0:
  broken = list(map(int, input().split()))
normal = list(map(lambda x: str(x) if x not in broken else None, range(10)))
normal = [x for x in normal if x is not None]

num = 500000
for i in range(500000):
  high = str(end + i)
  if all(map(lambda x : True if x in normal else False, high)):
    num = i + len(high)
    break

for i in range(end + 1):
  low = str(end - i)
  if all(map(lambda x : True if x in normal else False, low)):
    num = min(num, i + len(low))
    break

print(min(abs(start-end), num))
N = int(input())

from itertools import permutations
HELLO = list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4))

result = []
# 가능한 모든 hello에 대해 경우의 수 판단 ( 10P4로 경우의 수가 가장 작기 때문 ) 
for H, E, L, O in HELLO:
  # h가 0일 때
  if H == '0':
    continue
  hello = H + E + L + L + O
  
  # N이 hello보다 작을 때 (world가 음수일 때)
  if N < int(hello):
    continue
  
  # w가 0일 때
  world = str(N - int(hello))
  if len(world) != 5:
    continue
  w, o, r, l, d = [x for x in world]

  # o자리가 다르거나 l자리가 다를 때
  if O != o or L != l:
    continue

  # w, r, d가 중복되는 경우
  if (w in hello + r + d) or (r in hello + w + d) or (d in hello + w + r):
    continue
  result.append(hello)
  result.append(world)
  break

if len(result) != 0:
  print('  ' + result[0])
  print('+ ' + result[1])
  print('-------')
  if N >= 100000:
    print(' ' + str(N))
  else:
    print('  ' + str(N))
else:
  print('No Answer')
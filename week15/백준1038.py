from itertools import combinations

Str_num = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
test = []
for i in range(1, 11):
  test += reversed(list(combinations(Str_num, i)))

N = int(input())
if len(test) <= N:
  print(-1)
else:
  print(''.join(test[N]))
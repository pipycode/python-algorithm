one = input()
two = input()
DP = [[0] * len(one) for _ in range(len(two))]

for i in range(len(one)):
  if one[i] == two[0]:
    DP[0][i] = 1

for i in range(len(two)):
  if one[0] == two[i]:
    DP[i][0] = 1

maxi = 0
for i in range(1, len(two)):
  for j in range(1, len(one)):
    if one[j] == two[i]:
      DP[i][j] =  DP[i - 1][j - 1] + 1
      if maxi < DP[i][j]:
        maxi = DP[i][j]
print(maxi)
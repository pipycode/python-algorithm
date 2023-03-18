N = int(input())

prime_find = [True] * (N + 1)
prime_find[0] = False
prime_find[1] = False

for i in range(2, N):
  if prime_find[i] == True:
    j = 2
    while(i * j) <= N:
      prime_find[i * j] = False
      j += 1

prime_num = [i for i in range(len(prime_find)) if prime_find[i]]

start = 0
sum = 0
answer = 0
for i, num in enumerate(prime_num):
  sum += num
  if sum == N:
    answer += 1
  elif sum > N:
    while sum > N:
      sum -= prime_num[start]
      start += 1
    if sum == N:
      answer += 1

print(answer)
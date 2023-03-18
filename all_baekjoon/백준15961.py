from sys import stdin
input = stdin.readline

N, d, k, c = map(int, input().split())
suisi = [int(input()) for _ in range(N)]

for i in range(k):
  suisi.append(suisi[i])

# 처음 상태
from collections import Counter
suisi_num = Counter(suisi[:k])
# 쿠폰 추가
suisi_num[c] += 1

# 슬라이딩?
cnt = len(suisi_num)
maxi = 0
for start in range(N):
  suisi_num[suisi[start]] -= 1
  if suisi_num[suisi[start]] == 0:
    cnt -= 1
  
  suisi_num[suisi[start + k]] += 1
  if suisi_num[suisi[start + k]] == 1:
    cnt += 1
    
  if cnt > maxi:
    maxi = cnt
  
print(maxi)
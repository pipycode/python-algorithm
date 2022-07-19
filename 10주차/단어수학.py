from collections import defaultdict

N = int(input())
alphaList = []
alpha = defaultdict(int)
for i in range(N):
    put = input()
    alphaList.append(put)
alphaList.sort(key=len, reverse=True)
while(len(alphaList)!=0):
    if len(alphaList[0]) == 1:
        if alphaList[0] in alpha.keys() :
            alpha[alphaList[0]] += 10 ** (len(alphaList[0])-1)
            alphaList.pop(0)
            continue
        alpha[alphaList[0]] += 10 ** (len(alphaList[0])-1)
        alphaList.pop(0)
    else:
        if alphaList[0][0] in alpha.keys() :
            alpha[alphaList[0][0]] += 10 ** (len(alphaList[0])-1)
            alphaList[0] = alphaList[0][1:]
            alphaList.sort(key=len, reverse=True)
            continue
        else:
            alpha[alphaList[0][0]] += 10 ** (len(alphaList[0])-1)
            alphaList[0] = alphaList[0][1:]
        if alphaList[0] == '':
            alphaList.pop(0)
        alphaList.sort(key=len, reverse=True)

print(alpha)
alpha = sorted(alpha.values(),reverse=True)
SUM = 0
for i in range(len(alpha)):
    SUM += alpha[i] * (9-i)
print(SUM)
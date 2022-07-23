from itertools import permutations
NUM = [ i for i in range(10)]
com_NUM = list(permutations(NUM,7))

def solution():
    N = int(input())
    for com in com_NUM:
        alphas = [ i for i in com] # 0d 1e 2h 3l 4o 5r 6w
        # N = (alphas[2]+alphas[6])*10000 + (alphas[1]+alphas[4])*1000 + (alphas[5]+alphas[3])*100 + (alphas[3]+alphas[3]) * 10 + alphas[4]+alphas[0]
        SUM = alphas[0] + alphas[1]*1000 + alphas[2]*10000 + alphas[3]*120 + alphas[4]*1001 + alphas[5]*100 + alphas[6]*10000
        
        if alphas[2] != 0 and alphas[6] != 0 and SUM == N:
            print('  ',alphas[2],alphas[1],alphas[3],alphas[3],alphas[4], sep='')
            print('+ ',alphas[6],alphas[4],alphas[5],alphas[3],alphas[0], sep='')
            print('-------')
            print(str(N).rjust(7))
            return
    print('No Answer')

solution()
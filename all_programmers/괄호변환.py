def change(s):
    if s == '(': return ')'
    else:        return '('

def step2(w):
    l, r, check = 0, 0, True
    for data in w:
        if data == '(': l += 1
        else:           r += 1
        if l < r: check = False
        elif l == r: break
    u = w[:l+r]
    v = w[l+r:]
    return u, v, check
        
def step3_step4(w):
    if len(w) == 0:
        return ''
    u, v, check = step2(w)
    if check:
        return u + step3_step4(v)
    else:
        temp = '(' + step3_step4(v) + ')' + ''.join(map(change, u[1:-1]))
        return temp

def solution(p):
    answer = ''
    answer = step3_step4(p)
    
    return answer
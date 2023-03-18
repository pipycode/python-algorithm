def calculate_expression(oper, num, expression):
    if num == 2:
        return str(eval(expression))
    elif oper[num] == '*':
        result = eval('*'.join([calculate_expression(oper, num+1, e) for e in expression.split('*')]))
    elif oper[num] == '+':
        result = eval('+'.join([calculate_expression(oper, num+1, e) for e in expression.split('+')]))
    elif oper[num] == '-':
        result = eval('-'.join([calculate_expression(oper, num+1, e) for e in expression.split('-')]))
    return str(result)

from itertools import permutations
def solution(expression):
    answer = 0
    for oper in permutations(['+', '*', '-']):
        result = int(calculate_expression(oper, 0, expression))
        answer = max(answer, abs(result))            
    return answer
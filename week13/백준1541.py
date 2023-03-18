math_exp = input().split('-')
result = [sum(map(int, plus.split('+'))) for plus in math_exp]

for data in result[1:]:
  result[0] -= data

print(result[0])
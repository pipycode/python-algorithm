N = int(input())
Test = list(map(int, input().split()))
if N == 1:
  print('A')
if N == 2:
  if Test[0] == Test[1]:
    print(Test[0])
  else:
    print('A')
elif N >= 3:
  # 1. a2 == a1일때
  if Test[1] == Test[0]:
    a = 1.0
    b = 0.0
  else:
    a = (Test[2] - Test[1]) / (Test[1] - Test[0])
    b = Test[1] - Test[0] * a
  # 2. a, b는 반드시 정수임
  if a.is_integer() and b.is_integer():
    # 3. 주어진 배열이 반드시 규칙을 만족한다는 보장이 없음
    if all([Test[i - 1] * a + b == Test[i] for i in range(1, len(Test))]):
      print(int(a * Test[len(Test) - 1] + b))
    else:
      print('B')
  else:
    print('B')
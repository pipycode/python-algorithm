N = int(input())                      # N <= 50
MAP = tuple(map(int, input().split())) # Height <= 1,000,000,000

def CanSee(index):
  Now = MAP[index]
  Forward = MAP[index + 1:]
  Backward = MAP[:index]

  num = 0
  if index < len(MAP) - 1:
    grad = -1000000000
    for i, building in enumerate(Forward, start=1):
      grad_temp = (building - Now) / i
      if grad_temp > grad:
        num += 1
        grad = grad_temp
      else:
        continue
  if index >= 1:
    grad = -1000000000
    for i, building in enumerate(reversed(Backward), start=1):
      grad_temp = (building - Now) / i
      if grad_temp > grad:
        num += 1
        grad = grad_temp
      else:
        continue
  return num

see = max(map(CanSee, range(len(MAP))))
print(see)
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.out = False

def dist_a_b(a:point, b:point):
    return abs(a.x-b.x) + abs(a.y-b.y)

def find_target(archer:point, enemy_list:list, D):
    m =1000
    m_i = -1
    for i, enemy_point in enumerate(enemy_list):
    # 적이 살아 있고 맵에 존재해야 공격할 수 있음
        if enemy_point.alive and not enemy_point.out:
            distance_to_target = dist_a_b(archer, enemy_point)
    # 적이 사정거리 안에 있어야 공격할 수 있음
            if distance_to_target <= D:
    # 제일 가까운 것부터 공격
                if distance_to_target < m:
                    m = distance_to_target
                    m_i = i
    return m_i

def simulation(archer_list:list, enemy_list:list, D):
    # 1. 모든 궁수들이 공격할 적을 정한다.
    attack_list = []
    for archer_point in archer_list:
        i = find_target(archer_point, enemy_list, D)
        if i != -1:
            attack_list.append(i)
    # 2. 공격
    for attack_index in attack_list:
        enemy_list[attack_index].alive = False
    # 3. 적의 이동
    for i in range(len(enemy_list)):
        if enemy_list[i].alive and not enemy_list[i].out:
            enemy_list[i].x += 1
            if enemy_list[i].x >= N:
                enemy_list[i].out = True

def num_enemy(enemy_list:list):
    result = 0
    for enemy in enemy_list:
        if enemy.alive and not enemy.out:
            result += 1
    return result

N, M, D = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

enemy_list = [point(i, j) for i in range(N) for j in range(M) if ground[i][j] == 1]
enemy_list.sort(key=lambda p:(p.y, -p.x))

from itertools import combinations
from copy import  deepcopy
result = 0
for a, b, c in combinations(range(M), 3):
    archer_list = [point(N, a), point(N, b), point(N, c)]
    temp_enemy_list = deepcopy(enemy_list)
    while num_enemy(temp_enemy_list):
        simulation(archer_list, temp_enemy_list , D)
    result = max(result, sum([1 for p in temp_enemy_list if not p.alive]))
print(result)
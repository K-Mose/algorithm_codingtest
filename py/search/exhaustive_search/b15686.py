"""
치킨배달
https://www.acmicpc.net/problem/15686

0 - 빈칸
1 - 집
2 - 치킨집

맨하탄거리문제?
|x1-x2| + |y1-y2|
"""


def get_d(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


N, M = map(int, input().split())
home = []
chicken = []
check = {}

for i in range(N):
    c = list(map(int, input().split()))
    for j in range(N):
        if c[j] == 1:
            home.append([i, j])
        elif c[j] == 2:
            chicken.append([i, j])

# 아래처럼 풀었을 때 최소 치킨거리지만 M개만 남겼을 때 치킨거리가 최소가 아닐 수 있다.
# 풀이처럼 순열로 최소 구하는 것이 맞다.
# # 각 지점별 치킨거리 구해서 나열하기
# for ck in chicken:
#     distance = 0
#     for hm in home:
#         distance += get_d(ck, hm)
#     if distance not in check.keys():
#         check[distance] = []
#     check[distance].append(ck)
#
# survived = []
# # 최소 치킨거리인 M개의 가게만 살리기
# for k in sorted(check.keys()):
#     if len(survived) >= M:
#         break
#     for c in check[k]:
#         if len(survived) >= M:
#             break
#         survived.append(c)
#
# # 집에서 가장 가까운 치킨거리 구하기
# chicken_distance = 0
# for h in home:
#     d = 50*50
#     for s in survived:
#         d = min(d, get_d(h, s))
#     chicken_distance += d
#
# print(chicken_distance)


# 풀이
"""
치킨집 최대 개수 13개
최대 연산 수 13 C M, 
13 C 7 , 13 C 6 = 1716

집 최대 100개
최대 연산
100 * 7 * 1716 = 1201200 
"""
from itertools import combinations

N, M = map(int, input().split())
houses = []
chickens = []

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        if v == 2:
            chickens.append((i, j))

# 도시의 치킨거리의 최소값 갱신
ans = 2 * N * len(houses)
for combi in combinations(chickens, M):
    tot = 0
    for house in houses:
        tot += min(get_d(house, chicken) for chicken in combi)
    ans = min(ans, tot)

print(ans)
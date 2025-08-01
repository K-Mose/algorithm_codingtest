"""
기타 콘서트
"""

# AND 연산으로 기타를 조합해서 최소 개수 구하기

from itertools import combinations
from functools import reduce

N, M = map(int, input().split())
scores = []
for _ in range(N):
    scores.append(int(input().split()[1].replace('Y', '1').replace('N', '0'), 2))
# 최대 연주
MAX = reduce(lambda x, y: x | y, scores)
# 연주 할 수 없음
if MAX == 0:
    print(-1)
else:
    for i in range(1, N + 1):
        for combi in combinations(scores, i):
            c = reduce(lambda x, y: x | y, combi)
            # reduce 없이
            # p = 0
            # for c in combi:
            #     p |= c
            if c == MAX:
                print(len(combi))
                exit()

# 비트마스킹 개념이 좀 익숙해진듯
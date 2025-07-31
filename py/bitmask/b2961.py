"""
# 문제
도영이는 짜파구리 요리사로 명성을 날렸었다. 이번에는 이전에 없었던 새로운 요리에 도전을 해보려고 한다.

지금 도영이의 앞에는 재료가 N개 있다. 도영이는 각 재료의 신맛 S와 쓴맛 B를 알고 있다. 여러 재료를 이용해서 요리할 때,
그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.

시거나 쓴 음식을 좋아하는 사람은 많지 않다.
도영이는 재료를 적절히 섞어서 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다.
또, 물을 요리라고 할 수는 없기 때문에, 재료는 적어도 하나 사용해야 한다.

재료의 신맛과 쓴맛이 주어졌을 때, 신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오.

# 입력
첫째 줄에 재료의 개수 N(1 ≤ N ≤ 10)이 주어진다.
다음 N개 줄에는 그 재료의 신맛과 쓴맛이 공백으로 구분되어 주어진다.
모든 재료를 사용해서 요리를 만들었을 때, 그 요리의 신맛과 쓴맛은 모두 1,000,000,000보다 작은 양의 정수이다.
"""

"""
10
1 7
2 6
7 8
4 9
1 7
2 6
7 8
4 9
2 8
5 9
"""
# # 조합 사용
# import math
# from itertools import combinations
#
# N = int(input())
# sour = []
# bit = []
# for i in range(N):
#     s, b = map(int, input().split())
#     sour.append(s)
#     bit.append(b)
#
# # print(sour, bit)
# s = []
# b = []
# for i in range(1, N + 1):
#     diff = 0
#     for c1 in combinations(sour, i):
#         s.append(math.prod(c1))
#     for c2 in combinations(bit, i):
#         b.append(sum(c2))
#
# ans = 10**9
# for i in range(len(s)):
#     ans = min(ans, abs(s[i] - b[i]))
#
# print(len(s))
# print(ans)


# 비트 마스킹
"""
# 왜 비트 마스킹인지?

재료가 최대 10개밖에 안 되므로,
모든 조합을 탐색해도 2^10 = 1024개로 완전탐색이 가능합니다.

이때 조합을 만들 때,
비트마스크를 쓰면 각 재료를 사용할지 말지를 0/1로 표현할 수 있습니다:

예를 들어, 재료가 4개 있을 때:

비트마스크	선택된 재료
0001	4번 재료만
0110	2번, 3번
1111	전부 사용

이렇게 1부터 2ⁿ - 1까지 순회하면서
선택된 재료의 인덱스를 확인하고,
각 조합의 신맛과 쓴맛을 계산해 절댓값 차이를 비교하면 됩니다.



1개 일 때 
1 > 2 - 1, 1

2개일 때 
11 > 4 - 1, 3

3개일 때 
111 > 8 - 1, 7

4개일 때 
1111 > 16 - 1, 15

5개 일 때
11111 > 32 - 1, 31
"""
N = int(input())
sour = []
bit = []

for _ in range(N):
    s, b = map(int, input().split())
    sour.append(s)
    bit.append(b)

ans = float('inf')
for bitmask in range(1, 1 << N):
    s = 1
    b = 0
    for i in range(N):
        if bitmask & (1 << i):
            s *= sour[i]
            b += bit[i]
    ans = min(ans, abs(s - b))

print(ans)


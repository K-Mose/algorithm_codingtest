"""
# 문제
N개의 정수로 이루어진 수열이 있을 때,
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
주어지는 정수의 절댓값은 100,000을 넘지 않는다.
"""
N, S = map(int, input().split())
numbers = list(map(int, input().split()))


def combination(start, total):
    # 합으로 넘겨야 시간복잡도가 줄어듬
    if total == S:
        global count
        count += 1
    for i in range(start, N):
        total += numbers[i]
        combination(i + 1, total)
        total -= numbers[i]


count = 0
combination(0, 0)
# 공집합 제거
if S == 0:
    count -= 1
print(count)

# # 조합 사용
# from itertools import combinations
# count = 0
# result = set()
# for n in range(N):
#     for c in combinations(numbers, n+1):
#         if sum(c) == S:
#             count += 1
# print(count)
# exit()

"""
2 0
0 0

3 0
-1 1 0

3 3
1 2 3

5 0
0 0 0 0 0

5 0
0 0 0 0 1

5 5
1 2 3 4 5

10 8
-7 -4 -3 0 1 2 3 4 6 9 


1
1
2
3
4
5
5

2
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
9

3
1 2 3
1 2 4
1 2 5
2 3 4
2 3 5
2 4 5
3 4 5
7

4
1 2 3 4
1 2 3 5
2 3 4 5
3

5
1 2 3 4 5
1

5 -3
-1 -1 -1 -1 -1

20 10
-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10
"""
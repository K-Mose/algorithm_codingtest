"""
# 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

# 입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
"""
N, M = map(int, input().split())

check = [False] * (N + 1)
path = []
result = []


def backtracking():
    if len(path) == M and sorted(path) not in result:
        result.append(sorted(path))
        print(*path)
        return

    for i in range(1, N + 1):
        if not check[i]:
            check[i] = True
            path.append(i)
            backtracking()
            path.pop()
            check[i] = False


backtracking()

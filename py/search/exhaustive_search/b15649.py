"""
N과 M (1)
# 문제
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	138185	89009	55639	63.355%
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
result = []


def dfs(sequence, check):
    if len(sequence) == M:
        result.append(sequence)
        return
    for n in check:
        if n not in sequence:
            dfs(sequence + [n], [c for c in check if n != c])


for i in range(1, N+1):
    dfs([i], [n for n in range(1, N+1) if n != i])

for r in result:
    print(" ".join(map(str, r)))

if __name__ == '__main__':
    exit()
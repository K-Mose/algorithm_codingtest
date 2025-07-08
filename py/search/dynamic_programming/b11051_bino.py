N, K = map(int, input().split())
bino_map = [[0] * (N + 1) for _ in range(N + 1)]

# 바텀업
for n in range(N + 1):
    bino_map[n][0] = 1
    bino_map[n][n] = 1
    for k in range(n + 1):
        if bino_map[n][k] == 0 and n >= 1 and k >= 1:
            bino_map[n][k] = bino_map[n - 1][k - 1] + bino_map[n - 1][k]
            bino_map[n][k] %= 10007
print(bino_map[N][K])

# 풀이
# 탑다운
import sys

sys.setrecursionlimit(10 ** 7)

cache = [[0] * 1001 for _ in range(1001)]


def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)
        cache[n][k] %= 10007
    return cache[n][k]


print(bino(N, K))

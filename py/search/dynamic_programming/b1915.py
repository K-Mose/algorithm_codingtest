"""
가장 큰 정사각형
# 문제
n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오
0100
0111
1110
0010
위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.

# 입력
첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.
"""
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

"""
길이가 1인 정사각형부터 k인 정사각형 까지 칸을 비교한다.
k-1길이의 정사각형이 들어가는 위치를 찾고, k길이의 정사각형이 들어가는지 확인한다.
모든 칸에 들어가지 않으면 k-1칸을 반환, 들어가는 칸이 있으면 k+1길이의 정사각형을 확인
7 9
111111111
111111111
111011111
111111111
111110101
111111111
111111101

시간초과 -> 최악의 경우 O(N*M*K^2)
"""


def rect_check(n, m, k):
    # k길이이므로 n + k - 1, m + k -1이 N, M보다 작을 때만 확인
    if n + k + 1 < N and m + k + 1< M:
        for k1 in range(0, k + 1):
            # print('    ', n, m, k, ' // ', n + k1, m + k, arr[n + k1][m + k], arr[n + k1])
            if arr[n + k1][m + k] == '0':
                return False
        for k2 in range(0, k + 1):
            # print('    ', n, m, k, ' // ', n + k, m + k2, arr[n][m + k2])
            if arr[n + k][m + k2] == '0':
                return False
        if arr[n + k][m + k] == '0':
            return False
        # print('    ', n, m, k, ' // ', n + k, m + k, arr[n + k][m + k])
        return True
    return False


check = [False] * (N * M)
index = 0
for ar in arr:
    for a in ar:
        if a == '1':
            check[index] = True
        index += 1


for k in range(1, N+1):
    # print(k)
    temp = [False] * (N * M)
    if sum(check) == 0:
        print((k - 1) ** 2)
        break
    for i, v in enumerate(check):
        if v:
            # 좌표
            n = i // N
            m = i % M
            # print(n, m, k)
            temp[i] = rect_check(n, m, k)
    # print(check)
    check = temp


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dp = [[0] * M for _ in range(N)]
_max = 0
for n in range(N):
    for m in range(M):
        if arr[n][m] == '0':
            dp[n][m] = 0
        elif arr[n][m] == '1' and (n == 0 or m == 0):
            dp[n][m] = 1
        elif n > 0 and m > 0:
            _min = min(dp[n-1][m], dp[n-1][m-1], dp[n][m-1]) + 1
            dp[n][m] = _min

for n in range(N):
    for m in range(M):
        _max = max(dp[n][m], _max)

print(_max**2)


# 풀이
"""
모든 경우의 수를 볼 때 
1x1 사각형은 1000 * 1000개 있음
2x2 사각형은 999 * 999 개 있음
....
1000x1000 사각형은 1개 있음
-> 약 3억3천만번 연산

NxN 사각형은 N-1xN-1크기의 정사각형이 들어있음

DP(i, j) := i, j칸을 우하단으로 하는 저어사각형 최대 크기
DP(i, j) = min(DP(i, j-1), DP(i-1, j), DP(i-1, j-1)) + 1, if arr[i][j] == 1 
좌, 좌상단, 상단의 칸으 크기가 N-1로 모두 같을 때 크기가 N인 정사각형이 됨
혹은 인접(좌, 좌상단, 상단)칸의 최소값 + 1 크기의 정사각형이 됨  
ex)
111111111
111111111
111011111
111111111 
위 좌표에서 나오는 정사각형의 크기는 아래와 같이 표현됨 
111111111
122222222
122012333
122112344
5 1
0
0
1
0
0
"""


n, m = map(int, input().split())
arr = [input() for _ in range(n)]
dp = [[0] * m for _ in range(n)]
for j in range(m):
    if arr[0][j] == '1':
        dp[0][j] = 1

for i in range(1, n):
    if arr[i][0] == '1':
        dp[i][0] = 1

    for j in range(1, m):
        if arr[i][j] == '1':
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(dp[i][j], ans)

print(ans**2)
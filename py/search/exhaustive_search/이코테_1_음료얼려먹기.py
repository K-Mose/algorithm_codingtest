"""
음료수 얼려 먹기
# 문제
NxM 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때 얼음 트르이 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.

# 입력
- 첫 번째 줄에 얼음 틀에 세로의 길이 N과 가ㅏ로의 길이 M이 주어집니다.
- 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어집니다.

입력 예시
4 5
00110
00011
11111
00000

4 8
10101010
10101010
10101010
10101010

3 3
001
010
101

출력 에시
3
"""


def printice():
    for c in ice:
        print(c)
    print()


N, M = map(int, input().split())
ice = []
for _ in range(N):
    # ice.append([int(t) for t in input()])
    ice.append(list(map(int, input())))

count = 0


def dfs(i, j):
    global ice
    ice[i][j] = 1

    if i + 1 < N and ice[i + 1][j] == 0:
        dfs(i + 1, j)
    if j + 1 < M and ice[i][j + 1] == 0:
        dfs(i, j + 1)


for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            count += 1
            dfs(i, j)
            printice()

print(count)


# 답안 예시
n, m = map(int, input().split())
graph = []


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
         # 해당 노드 방문 처리
         graph[x][y] = 1
         dfs(x - 1, y)
         dfs(x + 1, y)
         dfs(x, y - 1)
         dfs(x, y + 1)
         return True
    return False


for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 실행
        if dfs(i, j):
            result += 1

print(result)

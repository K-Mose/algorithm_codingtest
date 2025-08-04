"""
미로 탈출
# 문제
동빈이는 NxM 킈의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
동빈이의 위치는 (1,1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다.
미로는 반드시 탈출 할 수 있는 형태로 제시됩니다.
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.

칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

# 입력
- 첫 줄에 두 정수 N, M이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수로 미로의 정보가 주어집니다.
각각의 수들은 공백없이 붙어서 입력으로 재시됩니다. 시작 칸과 마지막 칸은 항상 1입ㄴ다.

입력 예시
5 6
101010
111111
000001
111111
111111

출력 예시
10

4 5
10111
10101
10101
11101
"""


# def printmaze():
#     for m in maze:
#         print(m)
#     print()
#
#
# # 입력받은 미로를 사용하여
# N, M = map(int, input().split())
# maze = []
# for _ in range(N):
#     maze.append(list(map(int, input())))
# count = 0
#
#
# def dfs(i, j):
#     maze[i][j] = 0
#     print(i, j)
#     printmaze()
#     global count
#     count += 1
#     if i == N - 1 and j == M - 1:
#         print(count)
#         exit()
#     if i > 0 and maze[i - 1][j] == 1:
#         maze[i - 1][j] = 0
#         dfs(i - 1, j)
#         maze[i - 1][j] = 1
#         count -= 1
#     if i + 1 < N and maze[i + 1][j] == 1:
#         maze[i + 1][j] = 0
#         dfs(i + 1, j)
#         maze[i + 1][j] = 1
#         count -= 1
#
#     if j > 0 and maze[i][j - 1] == 1:
#         maze[i][j - 1] = 0
#         dfs(i, j - 1)
#         maze[i][j - 1] = 1
#         count -= 1
#     if j + 1 < M and maze[i][j + 1] == 1:
#         maze[i][j + 1] = 0
#         dfs(i, j + 1)
#         maze[i][j + 1] = 1
#         count -= 1
#
#
# dfs(0, 0)
# print(count)
# # 인접 행렬로 변경 후?
# adj = [[0] * M for _ in range(N)]
# print(adj)



# 답안 예시
from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # 큐 구현
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4 방향으로이동 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # 넓이 우선순위는 각 지점마다 도달하는 수가 최단거리기 때문에
                # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]



print(bfs(0, 0))
for g in graph:
    print(g)

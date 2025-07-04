"""
# 문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v)
같은 간선은 한 번만 주어진다.
"""
# 인접 리스트로
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
# 1. 간선들을 그래프로 만듬
graph = {i + 1: [] for i in range(N)}
for edge in edges:
    x = edge[0] - 1
    y = edge[1] - 1
    graph[x + 1] += [y + 1]
    graph[y + 1] += [x + 1]


# 2. 그래프를 탐색하여 연결 요소 개수 구함
def search_graph(node):
    # global visited
    if node in visited:
        return
    visited.append(node)
    for _node in graph[node]:
        search_graph(_node)


visited = []
cc = 0
for i in range(N):
    if i+1 not in visited:
        cc += 1
    search_graph(i+1)
print(cc)



# 코딩선배 풀이
# 행렬로
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    graph[a][b] = graph[b][a] = 1

ans = 0
chk = [False] * N
print(chk[0])


def dfs(node):
    for nxt in range(N):
        print(chk[0])
        print(chk[nxt])
        if graph[node][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)









if __name__ == "__main__":
    exit()

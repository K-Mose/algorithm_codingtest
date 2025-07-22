"""
# 문제
케빈 베이컨 6단계 법칙
케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다.
둘째 줄부터 M개의 줄에는 친구 관계가 주어진다. 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다.
A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다.
친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다.
또, 모든 사람은 친구 관계로 연결되어져 있다. 사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.


최단거리 - bfs
"""


# 출이
"""
케인 베이컨의 수를 번호마다 구한 후 
순차탐색으로 가장 작은 번호를 구한다. 

kevin = []

1 - 3 - 4 - 9
1 - 7 - 9 2번만에 도달

1 - 2
1 - 3
1 - 4
... 
1 - N, 
1번의 케빈베이컨 수 

2 - 1
2 - 3 
2 - 4
...
2 - N, 
2번의 케빈베이컨 수

3번의 케빈베이컨 수 ...
N번의 케빈베이컨 수를 구해서 kevin 배열에 넣고 가장 작은 수의 인덱스를 구한다. 


두 노드간 최단거리 수는 

"""
from collections import deque

N, M = map(int, input().split())
# 인접 노드로 구현
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)


kevin = []
ans = (-1, 10000)


def bfs(start, goal):
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d

        nd = d + 1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, nd))


def get_kevin(start):
    tot = 0
    for i in range(N):
        if i != start:
            tot += bfs(start, i)
    return tot


for i in range(N):
    kevin.append(get_kevin(i))


for i, v in enumerate(kevin):
    if ans[1] > v:
        ans = (i, v)

print(ans[0] + 1)




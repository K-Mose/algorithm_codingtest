# 완전 탐색

- 장점 : 반드시 답을 찾을 수 있다. 
  - 전부 살피기 때문에 답을 찾음
- 단점
  - 시간이 오래 걸리고 리소스를 많이 잡아먹는다. 
- 컴퓨터 자원 <-> 시간의 trade-off 관계


### 브루트 포스 Brute-force (무차별 대입법)
- ex: 비밀번호 4자리에서 경우의 수 10^4가지(0000~9999)를 전부 넣어 보면 뚫림
- 암호학, 수학 등 학계에서도, PS에서도 널리 쓰이는 알고리즘
- 4색정리 증명에도 쓰였다. 

`문제: N개의 수를 입력 받아서 두 수를 뽑아 합이 가장 클 때는?`
N개의 숫자에서 쌍을 만드는 모든 경우의 수를 찾아서 비교할 수 있다. (경우의 수는 nC2, 시간 복잡도는 O(N^2))

만약 시간 제한 2초, 입력: 2 <= N <= 1,000,000 이라고 한다면 , 시간 복잡도가 10^12이므로 시간 초과되어 실패하게 된다. 

이 때는 입력값을 정렬하여 가장 큰 두 수를 찾을 수 있다. 
혹은 순열, 조합의 라이브러리 또는 함수를 사용하여 찾을 수 있다.  
```python
# 순열
from itertools import permutations
v = [0, 1, 2, 3]
for i in permutations(v, 4):
    print(i)

# 조합 
from itertools import combinations
v = [0, 1, 2, 3]
for i in combinations(v, 2):
    print(i)
```



## 그래프 Graph
- 노드(node, 혹은 vertex)와 간선(edge)로 이루어진 도표
- 무방향 그래프: 간선에 방향성이 없는 그래프, 양방향 그래프와 동일
- 방향 그래프: 단방향으로 간선의 방향이 있는 그래프
- 순환 그래프: 그래프에서 순환(Cycle)이 있는 그래프, 
- 비순환 그래프: 순환이 없는 그래프

### 트리 Three
- 트리는 순환성이 없는 무방향 그래프
- 특정하지 않은 한 어떤 노드든지 루트가 될 수 있다. 
- 가장 바깥쪽 노드는 리프노트 
- node A에서 node B로 가는 경로는 반드시 존재하며 유일하다.
- 노드개수 = 간선개수 + 1

### 코드를 그래프로 나타내는 방법 
1. 인접 행렬
  - 노드로 행, 열을 표현하고, 노드간 간선의 유무를 0, 1로 표현. (양방향일 경우 대칭 행렬의 모습)
2. 인접 리스트
  - 시작 노드별로 연결된 노드를 연결 리스트로 표현

#### 인접 행렬 vs 인접 리스트
- 비교
  - 인접 행렬이 공간을 더 많이 차지함(노드가 N개면 N^2개 만큼 공간을 차지), 하지만 노드간 연결을 확인하는 시간적 측면에서는 더 유리함 
  - 인접 리스트는 간선이 없으면 메모리를 아낄 수 있지만, 간선이 많은 그래프에서는 시간이 많이 소모된다. 

### DFS Depth First Search 깊이 우선 탐색
- 스택 or 재귀를 사용해서 구현
```python
adj = [[0] * 13 for _ in range(13)] # 13x13의 인접 행렬의 간선이 연결되었다 할 때 

def dfs(now):
    for nxt in range(13):
      if adj[now][nxt]:
        dfs(nxt)
            
dfs(0)
```

### BFS Breadth First Search 너비 우선 탐색
- 큐를 사용해서 구현
- 최단거리 문제에서 자주 사용 
```python
from collections import deque

def bfs():
    dq = deque
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

bfs()
```

길찾기 문제 에
```python
from collections import deque

# 방향
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
# 방문 체크
chk = [[False] * 100 for _ in range(100)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
      y, x = q.popleft()
      chk[y][x] = True
      for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        # 유효한 칸이면서 방문하지 않은 칸이면 방문
        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            q.append((ny, nx))
```

### 백트래킹 Backtracking
- 모든 경우를 탐색하며 DFS/BFS 방식과 유사하다.
- 백트래킹은 가지치기를 통해 탐색 경우의 수를 줄인다는 차이가 있다. 
  - 최악의 경우, 모든 경우를 다 살펴보게 될 수 있지만 가능한 덜 보겠다는 전략
  - '가망성이 없으면 가지 않는다.'
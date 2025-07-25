"""
색종이 붙이기
# 문제
<그림 1>과 같이 정사각형 모양을 한 다섯 종류의 색종이가 있다. 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.
색종이를 크기가 10×10인 종이 위에 붙이려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다. 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.

종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.

# 입력
총 10개의 줄에 종이의 각 칸에 적힌 수가 주어진다.
"""

"""
가장 큰 종이부터 덮어보면서
될때까지 반복
"""
arr = []
for _ in range(10):
    arr.append(list(map(int, input().split())))


def check_sum(c):
    s = 0
    for _c in c:
        s += sum(_c)
    return s == 0


def cover(i, j, paper, check):
    if paper + j <= 10 and paper + i <= 10:
        for p1 in range(paper):
            for p2 in range(paper):
                if check[i + p1][j + p2] == 0:
                    return 0
        print(f'cover:: [{i}, {j}]: {paper}')
        return 1
    return 0


def find(paper, check, count):
    print('find:', paper, check_sum(check), count, used)
    if check_sum(check):
        print(sum(used), used, count)
        for c in check:
            print(c)
        return sum(used)

    if count < 1 and paper > 2:
        return find(paper - 1, check, 5)
    if count < 1 and paper < 2:
        return -1
    # 2. 종이로 덮을 공간 찾기
    _check = [c[:] for c in check]
    for i in range(10):
        for j in range(10):
            if _check[i][j] == 1:
                used[paper - 1] += 1
                result = cover(i, j, paper, _check)
                if result == 0:
                    used[paper - 1] -= 1
                else:
                    # 3. 찾으면 덮기
                    for p1 in range(paper):
                        for p2 in range(paper):
                            _check[i + p1][j + p2] = 0
                    for i in range(10):
                        print(check[i], _check[i])
                    # 4. 다음 종이로 공간 찾기
                    return find(paper, _check, count - 1)
    print(f'{paper} can\'t find')
    return find(paper - 1, check, 5)


used = [0, 0, 0, 0, 0]
# 완전 탐색으로 모든 경우 다 저장
result = [-1, -1, -1, -1, -1]
# 1. 종이 선택
for p in range(5, 0, -1):
    check = [a[:] for a in arr]
    for i in range(10):
        print(check[i])
    print(f'p:{p}')
    result[p-1] = find(p, check, 5)
    print(f'{p}:: {result[p-1]}, {result}')
    used = [0, 0, 0, 0, 0]
print('result', result)
_min = 25
for r in result:
    if r != -1:
        _min = min(_min, r)
if _min == 25:
    print(-1)
else:
    print(_min)

"""
순서
1. 종이 선택
2. 종이로 덮을 공간 찾기
3. 찾으면 덮기 (덮인 공간 체크)
4. 다음 종이로 공간 찾기
5. 없으면 한칸 작은 종이 선택
6. 2-5 반복하다가 종이 없으면 종료


흠.. 21%에서 틀림..
"""


# 풀이
"""
기본적으로 2중 반복문으로 탐색하다가 1을 만나면 종이를 덮어보며 찾아본다. 
그리디로 하면 8x8 크기에서 반레가 생긴다.  https://www.acmicpc.net/board/view/57010
0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
결국 모든 종이를 다 해봐야 한다.
작은 종이부터 붙여가면서 안붙으면 다음 종이 써보면서 되돌아가는 백트래킹으로 구현한다. 
"""

board = [list(map(int, input().split())) for _ in range(10)]
# 모든 종이 다 쓸 때 25장
ans = 25
paper = [0] * 6  # 색종이 크기 1 .. 5 까지 사용 횟수


def is_possible(y, x, sz):
    # 색종이 개수 체크
    if paper[sz] == 5:
        return False

    # 범위 체크
    if y + sz > 10 or x + sz > 10:
        return False

    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False
    return True


def mark(y, x, sz, v):
    for i in range(sz):
        for j in range(sz):
            board[y + i][x + j] = v
    if v:
        paper[sz] -= 1
    else:
        paper[sz] += 1


# 각각의 좌표를 받는 행렬
def backtracking(y, x):
    # 모든 좌표 다 돌았을 떄
    global ans
    if y == 10:
        ans = min(ans, sum(paper))
        return
    # 다음줄로 넘어감
    if x == 10:
        backtracking(y + 1, 0)
        return

    if board[y][x] == 0:
        backtracking(y, x + 1)
        return
    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)  # 색종이 덮기
            backtracking(y, x + 1)  # 다음칸으로 진행
            mark(y, x, sz, 1)  # 원상복구


backtracking(0, 0)
print(ans if ans != 25 else -1)

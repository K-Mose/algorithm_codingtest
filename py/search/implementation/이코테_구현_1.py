"""
상하좌우 문제
# 문제
여행가 A는 N x N 크기의 정사각형 공간 위에 있습니다. 이 공간은 1x1 크기의 정사각형으로 나누어져 있습니다.
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다.
여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다.
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여있습니다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있습니다.
각 문자의 의미는 다음과 같습니다.
- L: 왼쪽으로 한 칸 이동
- R: 오른쪽으로 한 칸 이동
- U: 위로 한 칸 이동
- D: 아래로 한칸 이동

# 입력
첫 줄에는 공간의 크기 N이 주어진다.
둘째 줄에는 A가 이동할 여행계획서가 주어진다.

e.g)
6
R R R U D D
"""
N = int(input())
route = list(input().split())
location = (1, 1)


def move(direction):
    y, x = location
    if direction == 'R' and x < N - 1:
        return y, x + 1
    elif direction == 'L' and x > 1:
        return y, x - 1
    elif direction == 'U' and y > 1:
        return y - 1, x
    elif direction == 'D' and y < N - 1:
        return y + 1, x
    else:
        return location


for r in route:
    location = move(r)
    print(r, location)

print(*location)

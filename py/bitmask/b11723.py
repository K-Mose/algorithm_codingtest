"""
집합
# 문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

- add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
- remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
- check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
- toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
- all: S를 {1, 2, ..., 20} 으로 바꾼다.
- empty: S를 공집합으로 바꾼다.

# 입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

"""
# # 일반적으로 set으로 풀었을 떄는 시간초과가 난다.
N = int(input())

s = set()

for n in range(N):
    op = input()
    if op.startswith('all') or op.startswith('empty'):
        if op == 'all':
            for i in range(1, 21):
                s.add(i)
        elif op == 'empty':
            s.clear()
    else:
        op, i = op.split()
        i = int(i)
        if op == 'add':
            s.add(i)
        elif op == 'remove':
            if i in s:
                s.remove(i)
        elif op == 'toggle':
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        elif op == 'check':
            if i in s:
                print(1)
            else:
                print(0)

# bitmask 사용
'''
11111111111111111111 == (1 << 20) - 1 
int('11111111111111111111',2) => 1048575
1 => (1 << 0)
10 => 1 << 1
11 => (1 << 1) + 1
101 => (1 << 2) + 1
'''
import sys
# https://djm03178.tistory.com/21
# input = sys.stdin.readline 만 사용하면 56에서 에러
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
s = 0


def fmt(num):
    return format(num, '0>20b')


for n in range(N):
    op = input()
    if op.startswith('all') or op.startswith('empty'):
        if op == 'all':
            s = (1 << 20) - 1
        elif op == 'empty':
            s = 0
    else:
        op, i = op.split()
        i = int(i)
        if op == 'add':
            if 1 << (i - 1) & s != 1 << (i - 1):
                s |= 1 << (i - 1)
        elif op == 'remove':
            if 1 << (i - 1) & s == 1 << (i - 1):
                s ^= 1 << (i - 1)
        elif op == 'toggle':
            if 1 << (i - 1) & s != 1 << (i - 1):
                s |= 1 << (i - 1)
            else:
                s ^= 1 << (i - 1)
        elif op == 'check':
            if 1 << (i - 1) & s == 1 << (i - 1):
                print(1)
            else:
                print(0)
        print(f'{op:8}', f'{i:4}', fmt(s))

"""
# 문제
서로 다른 숫자와 문자로 이루어진 집합과 위치가 주어졌을 때,
그 집합의 순열 중 주어진 위치의 순열을 구하는 프로그램을 작성하시오.

# 입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있다.
첫 번째 문자열은 서로 다른 숫자와 알파벳으로 이루어져 있으며, 길이는 최대 10이다.
또한, 사전순 순서대로 주어진다.
문자열 다음에는 찾아야 하는 위치가 주어지며, 이 값은 3,628,800보다 작거나 같은 자연수이다.
"""
import time
from itertools import permutations
from math import factorial

depth = 0


# 직접 구현
def permutation(l, p, plist, used, finish):
    if len(l) == len(p):
        # print(p)
        global depth
        depth += 1
        if finish == depth:
            plist.append(''.join(p))
        return
    for i in range(len(l)):
        if not used[i]:
            used[i] = True
            p.append(l[i])
            permutation(l, p, plist, used, finish)
            if depth == finish:
                return plist
            p.pop()
            used[i] = False
    return plist


while True:
    try:
        string, no = input().split()
        count = 0
        depth = 0
        used = [False] * len(string)
        if factorial(len(string)) < int(no):
            print(f'{string} {no} = No permutation')
            continue
        s1 = time.time()
        per = permutation(string, [], [], used, int(no))
        e1 = time.time()
        print(e1-s1)
        print(f'{string} {no} = {"".join(per)}')


        # permutations 사용
        count = 0
        s2 = time.time()
        if factorial(len(string)) < int(no):
            print(f'{string} {no} = No permutation')
            continue
        for p in permutations(string):
            count += 1
            if count == int(no):
                e2 = time.time()
                print(e2 - s2)
                print(f'{string} {no} = {"".join(p)}')
                break
    except Exception as e:
        print(e)
        break

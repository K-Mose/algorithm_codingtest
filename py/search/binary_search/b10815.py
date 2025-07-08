"""
# 문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며,
이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다
"""
import sys
import bisect
input = sys.stdin.readline
N = int(input())
have = list(map(int, input().split()))
M = int(input())
doyouhave = list(map(int, input().split()))
have.sort()


def bisearch(start, end, search, cnt):
    if start > end:
        return 0
    m = (start + end) // 2
    if have[m] > search:
        return bisearch(start, m-1, search, cnt + 1)
    elif have[m] < search:
        return bisearch(m+1, end, search, cnt + 1)
    elif have[m] == search:
        return 1
    if start == end:
        return 0


check = [0] * M
for dyh_idx in range(M):
    check[dyh_idx] = bisearch(0, N-1, doyouhave[dyh_idx], 0)
    # bisect 사용한 이진탐색, 훨씬 빠르다
    # check[dyh_idx] = 1 if (bisect.bisect_right(have, doyouhave[dyh_idx]) - bisect.bisect_left(have, doyouhave[dyh_idx])) > 0 else 0
print(*check)


# 풀이
N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
qry = list(map(int, input().split()))
ans = []
for q in qry:
    l = bisect.bisect_left(cards, q)
    # 카드 존재 유무로 찾기
    ans.append(1 if cards[l] == q else 0)
    # r = bisect.bisect_r(cards, q)
    # ans.append(1 if r - l else 0)
print(*ans)
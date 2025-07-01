"""
# 문제
정렬된 두 묶음의 숫자 카드가 있다고 하자.
각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.
이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다.
이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다.
예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤,
합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다.
그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다.
숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.
"""

"""
1트
2진트리 형식의 구조로 만들어 계산
e.g) 
3 
10 
20 
40
0| 10 20 30
1| 40
=> 100

틀림, 반례가 많음
"""

def accumulate(a, b, _sum=True):
    global acc
    acc = a + b
    global sorting
    global sorting2
    if len(sorting2) > 1 and (len(sorting2[-1]) == 3 or len(sorting2[-2]) == 3):
        acc = sum([sorting2[-1][-1] + sorting2[-2][-1]])
        sorting2.append([sorting2[-1][-1] + sorting2[-2][-1]])
    sorting.append(a+b)
    if _sum:
        sorting2.append([a, b, a+b])
    else:
        sorting2.append([b])
    return acc


N = int(input())
cards = [int(input()) for _ in range(N)]
# cards.sort(reverse=True)
# sorting = []
# sorting2 = []
# acc = 0
# if N == 1:
#     print(0)
# elif N == 2:
#     print(sum(cards))
# else:
#     while cards:
#         if not sorting or (len(cards) > 1 and sum(cards[-2:]) < acc):
#             acc = accumulate(cards[-1], cards[-2])
#             cards = cards[:-2]
#         else:
#             acc = accumulate(acc, cards[-1], _sum=False)
#             cards = cards[:-1]
#     print(sorting2)
#     print(sum([sum(a) for a in sorting2]))

"""
2트
list로 구현 => 시간초과
"""

if N == 1:
    print(0)
else:
    acc = 0
    while len(cards) > 1:
        a = cards.pop(cards.index(min(cards)))
        b = cards.pop(cards.index(min(cards)))
        acc += a + b
        cards.append(a + b)

    print(acc)

"""
3트
우선순위 큐 적용,
시간 초과 해결,
"""
import heapq

if N == 1:
    print(0)
else:
    heapq.heapify(cards)
    acc = 0

    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        acc += a + b
        heapq.heappush(cards, a + b)


    print(acc)
if __name__ == '__main__':
    exit()
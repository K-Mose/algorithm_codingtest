"""
모험가 공포도
N 명의 모험가가 여행을 떠나는데
각 모험가는 공포도를 가지며, 공포도 이상의 모험가 수와 함께 모험을 해야 한다.
이때 만들 수 있는 최대 그룹 수는?

# 입력
모험가 수 N개가 주어지고, 다음 줄에 N명의 공포도가 한줄로 주어진다.

e.g)
5
2 1 3 2 2
"""
N = int(input())
X = list(map(int, input().split()))
group = []
party = []
for x in sorted(X):
    party.append(x)
    if len(party) >= x:
        group.append(party[:])
        party = []
print(len(group))
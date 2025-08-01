"""
물병
"""

"""
N개의 물병을 같은 양을 합쳐서 다음 무게로 만들어서 총 K개의 물병으로 만듦

 
K의 물병은 K/2 + K/2 물병의 합

만들 수 있는 물병 
1, 2, 4, 8, 16, 24, ...

2의 거듭제곱의 용량은 1개로 만들 수 있다. 

10^7보다 작은 수 이므로 
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
...
2^22 = 4194304
2^23 = 8388608
2^24 = 16777216

2의 23제곱 부터 계산 가능
1. K-1번 만큼 N을 2의 거듭제곱으로 빼기 
2. 뺸 수를 가장 작은 거듭제곱으로 만들어서 새로운 병으로 합산
"""
# N, K = map(int, input().split())
# bottles = []
# for i in range(24, 0, -1):
#     if N >= 2 ** i:
#         print(N)
#         bottles.append(2 ** i)
#         N -= 2 ** i
# if N > 0:
#     bottles.append(N)
# print(bottles, N)
# if len(bottles) <= K:
#   print(0)
# elif len(bottles) > 1:
#     print(f'{bottles[K - 1]} - {sum(bottles[K:])} // {bottles[K:]}')
#     print(bottles[K-1] - sum(bottles[K:]))

# 비트 마스킹으로 풀기
# 합치는 물병의 수는 2의 거듭제곱이므로 비트바스킹으로 할 수 있다.
# 비트로 변환 했을 때 1인 자리수의 합이 K개 이하가 되게 하면 된다.
N, K = map(int, input().split())

bit = format(N, '0b')
p = 0
f = False
exclusive = ''
for b in bit:
    p += 1
    if b == '1':
        if K > 0:
            K -= 1
        else:
            f = True
    if K <= 0:
        if b == '1':
            exclusive += '0'
        else:
            exclusive += '1'
exclusive = int(exclusive, 2)
if not f:
    print(0)
else:
    print(exclusive + 1)
# 비트마스킹이 맞는지 의문
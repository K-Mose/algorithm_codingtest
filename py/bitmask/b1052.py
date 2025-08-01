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
N, K = map(int, input().split())
bottles = []
for i in range(24, 0, -1):
    if N >= 2 ** i:
        print(N)
        bottles.append(2 ** i)
        N -= 2 ** i
if N > 0:
    bottles.append(N)
print(bottles, N)
if len(bottles) <= K:
  print(0)
elif len(bottles) > 1:
    print(f'{bottles[K - 1]} - {sum(bottles[K:])} // {bottles[K:]}')
    print(bottles[K-1] - sum(bottles[K:]))

"""
초콜릿 식사
"""

"""
D개의 정사각형 -> D/2 2개 

초콜릿 크기는 1,2,4,8,16...
2의 거듭제곱일 떄는 0

4 =  100   0번
5 =  101   3번
6 =  110   2번
7 =  111   3번
9 =  1001  4번
15 = 1111  4번
17 = 10001 5번
쪼개지는 개수는
마지막 1이 나온 수까지의 길이
"""
K = int(input())
# # 그리디
# exp = 0
# while K >= 2**exp:
#     if K / 2**exp == 1:
#         print(f'{2 ** exp} {0}')
#         exit()
#     exp += 1
# bit = format(K, '0b')
#
# bar = 1 << len(bit)
# split = 0
# for i in range(len(bit)):
#     if bit[i] == '1':
#         split = max(split, i + 1)
# print(f'{bar} {split}')

# 비트마스킹
bit = 0
while K >= (1 << bit):
    if (1 << bit) == K:
        print(f'{K} 0')
        exit()
    bit += 1
for i in range(K.bit_length()):
    if K >> i & 1:
        print(f'{(1 << bit)} {(K >> i).bit_length()}')
        break
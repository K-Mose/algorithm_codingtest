"""
이진수 연산
# 문제
총 100,000 비트로 이루어진 이진수 A와 B가 주어진다. 이때, A & B, A | B, A ^ B, ~A, ~B를 한 값을 출력하는 프로그램을 작성하시오.

# 입력
첫째 줄부터 한 줄에 하나씩 차례대로 A & B, A | B, A ^ B, ~A, ~B를 출력한다.
"""

'''
f-string padding
f'{var:{char}{left > | right <}{width}'

e.g)
a = 'abc'
print(f'{a:x>5}')
result: xxabc

b = '12345'
print(f'{a:0>8}')
print(f'{a:0<8}')
result: 00012345
result: 12345000
0001011000111
0000101111111
'''
a = input()
b = input()
l = len(a)
n = '1' * l

# 연산자
print(f'{int(a,2)&int(b,2):0{l}b}')
print(f'{int(a,2)|int(b,2):0{l}b}')
print(f'{int(a,2)^int(b,2):0{l}b}')
print(f'{int(n,2) - (int(a,2)):0{l}b}')
print(f'{int(n,2) - (int(b,2)):0{l}b}')
print()

# 계산 구현
result = ''
# A & B
for i in range(l):
    if a[i] == '1' and b[i] == '1':
        result += '1'
    else:
        result += '0'
print(result)
result = ''
# A | B
for i in range(l):
    if a[i] == '1' or b[i] == '1':
        result += '1'
    else:
        result += '0'
print(result)
result = ''
# A ^ B
for i in range(l):
    if a[i] == b[i]:
        result += '0'
    elif a[i] == '1' or b[i] == '1':
        result += '1'
print(result)
result = ''
# ~A
for i in range(l):
    if a[i] == '0':
        result += '1'
    else:
        result += '0'
print(result)
result = ''
# ~B
for i in range(l):
    if b[i] == '0':
        result += '1'
    else:
        result += '0'
print(result)
"""
문자열 재정렬
# 문제
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이 때 모든 알파벳을 오름차숫으로 정렬하여 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

K1KA5CB7
AJKDLSI412K4JSJ9D
"""
string = list(input())
string.sort()
a = ''
n = 0
for s in string:
    if 64 < ord(s) < 91:
        a += s
    else:
        n += int(s)

print(f'{a}{n}')
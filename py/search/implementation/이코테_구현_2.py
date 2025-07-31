"""
시각
# 문제
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.

# 입력
첫 줄에 정수 N이 입력됩니다. ( 0 <= N <= 23)
"""

# 모든 경우의 수는 24 * 60 * 60 = 86,400이므로 완전탐색 해도 빠르게 탐색 가능 

N = int(input())
count = 0
for h in range(0, N + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                count += 1
                # print(f'{h:02}시 {m:02}분 {s:02}초')
print(count)
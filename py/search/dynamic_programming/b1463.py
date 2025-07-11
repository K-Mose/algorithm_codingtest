"""
1로 만들기
# 문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
"""
X = int(input())
MAX = 10**6
check = [0] * (MAX + 1)
# 1일 때는 0번임
check[1] = 0
check[2] = 1
check[3] = 1

for x in range(1, X + 1):
    print()
    print(x, '=> ', check[x])
    if x * 2 <= MAX:
        check[x * 2] = check[x] + 1 if check[x * 2] == 0 else min(check[x * 2], check[x] + 1)
        print(x * 2, check[x * 2], check[x])
    if x * 3 <= MAX:
        check[x * 3] = check[x] + 1 if check[x * 3] == 0 else min(check[x * 3], check[x] + 1)
        print(x * 3, check[x * 3], check[x])
    if x + 1 <= MAX:
        check[x + 1] = check[x] + 1 if check[x + 1] == 0 else min(check[x + 1], check[x] + 1)
        print(x + 1, check[x + 1], check[x])
print(check[X])


"""
fn(x) -> min(fn(x/3), fn(x/2), fn(x-1))

fn(1) = 0
fn(2) = 1
fn(3) = 1
fn(4) = 2
fn(5) = 3
fn(6) = 2
fn(7) = 3
fn(8) = 3
fn(9) = 2
fn(10) = f()3 
fn(11) = fn(10) + 1 = 4
...

"""

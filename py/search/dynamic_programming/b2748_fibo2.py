n = int(input())
fibo = []
for i in range(n+1):
    if i == 0:
        fibo.append(0)
    elif i == 1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[n])


# # 재귀로 하면 캐싱을 하지 않았기 때문에 많은 시간이 소요된다.
# count1 = 0
# def ffibo(i):
#     global count1
#     count1 += 1
#     if i == 0:
#         return 0
#     elif i == 1:
#         return 1
#     else:
#         return ffibo(i-1) + ffibo(i-2)
#
#
# print(ffibo(n))
# print(count1)

# 풀이
cache = [-1] * (n+1)
cache[0] = 0
cache[1] = 1

count2 = 0


def f(i):
    global count2
    count2 += 1
    if cache[i] == -1:
        cache[i] = f(i - 1) + f(i - 2)
    return cache[i]


print(f(n))
print(count2)

"""
팰린드롬 만들기
# 문제
임한수와 임문빈은 서로 사랑하는 사이이다.

임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

# 입력
첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.
"""

"""
입력값을 순열로 만들어서 
알파뱃 순서대로 정렬 후 
앞뒤가 같은지 확인한 후 출력

없으면 암쏘리
=> 시간초과 
최악 50!/0! = 50! = 3.0414e+64 ...

암쏘리..
"""
# from itertools import permutations
#
# string = input()
#
#
# def check_front_back(s):
#     m = len(s) // 2
#     if s[:m] == s[-1:m-1:-1]:
#         return True
#     return False
#
# for p in permutations(string):
#     print(*p)
#     if check_front_back(p):
#         print(''.join(p))
#         exit()


"""
앞뒤가 같으려면 홀수개는 최소 1개만있어야 하고 홀수는 중앙에 있다. 
나머지는 다 짝수여야 한다. 
A~Z까지 map으로 갯술를 받아서 개수를 확인하고 
홀수가 2개 이상이면 암쏘리 출력
짝수의 1/2만큼 순서대로 출력 후 중앙에 홀수 1개 넣고 나머지 거꾸로 출력

ZZYYXXWWVVUUTTSSRRQQQPPPOOOKKJJIIHHGGFFEEDDCCBBAA
ZZYYXXWWVVUUTTSSRRQQPPOOKKJJIIHHGGFFEEDDCCBBAA
"""
test = 'ABCDEFGHIJKLMNOQPRSTUVWXYZABCDEFGHIJKLMNOQPRSTUVWXYZ'
print(''.join(sorted(test, reverse=True)))

abc = dict()
ILUVU = input()
for iluvu in ILUVU:
    if iluvu not in abc.keys():
        abc.update({iluvu: 1})
    else:
        abc[iluvu] += 1

odd_count = 0
odd = ''
front = ''
for k in sorted(abc):
    if abc[k] % 2 == 1:
        odd_count += 1
        odd = k
        if odd_count > 1:
            print("I'm Sorry Hansoo")
            exit()
    l = abc[k] // 2
    front += k * l

print(front + odd + front[::-1])
# 맞았음!!


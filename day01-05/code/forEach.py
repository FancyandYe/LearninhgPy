"""
100以内求和
"""
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)
"""
100以内偶数求和
"""
# sum = 0
# for x in range(0, 101, 2):
#     sum += x
# print(sum)
# sum = 0
# for x in range(0, 101):
#     if x % 2 == 0:
#         sum += x
# print(sum)
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入数字'))
#     if answer > number:
#         print('输入数字太小啦')
#     elif answer < number:
#         print('输入数字太大啦')
#     else:
#         print('输入正确')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你是猪吗')
"""
输出99乘法表
"""
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', i * j, end='\t')
#     print()
"""
判断一个数字是不是素数
"""
# from math import sqrt
# number = int(input('请输入需要检查的数字'))
# end = int(sqrt(number))
# pass_no = '不是素数'
# pass_yes = '是素数'
# is_prime = True
# for x in range(2, end + 1):
#     print(x)
#     if number % x == 0:
#         is_prime = False
#         break
# if is_prime and number != 1:
#     print(pass_no)
# else:
#     print(pass_yes)
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

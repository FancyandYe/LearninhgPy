"""
身份验证
"""
# username = input('请输入用户名')
# password = input('请输入密码')
# if username == 'admin' and password == '123456':
#     print('欢迎回家')
# else:
#     print('密码错误')
"""
分段函数
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
# x = float(input('请输入未知数x：'))
# if x > 1:
#     y = 3 * x - 5
# elif x < -1:
#     y = 5 * x + 3
# else:
#     y = x + 2
# print('y = ', int(y))
# x = float(input('请输入未知数x：'))
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x > -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
# print(int(y))
"""
练习题：投掷筛子决定吃什么
"""
from random import randint
face = randint(1, 3)
if face == 1:
    print('吃火锅')
elif face == 2:
    print('吃龙虾')
elif face == 3:
    print('吃螃蟹')
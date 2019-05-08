"""
练习使用数据类型
"""
# 练习1. 接受华氏度，输出摄氏度。F = 1.8C + 32
# f = float(input("请输入华氏度"))
# c = int((f - 32) / 1.8)
# print("摄氏度= ", c)

# 练习2. 输入圆的半径计算计算周长和面积
# 使用import 引入外部函数
# import math
# r = float(input("请输入圆的半径"))
# perimeter = int(2 * math.pi * r)
# area = int(math.pi * r ** 2)
# print("圆的周长=", perimeter)
# print("圆的面积=", area)

# 练习3. 输入年份判断是不是闰年
# year = int(input('请输入年份: '))
# is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(is_leap)
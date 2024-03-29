print("Hello world")

# 注释

''''
多行注释
'''

"""
多行注释
"""

# 缩进
if True:
    print("True")
else:
    print("False")

# 多行
total = 1 + \
        2 + \
        3
print('多行结果 : ' + str(total))

# 字符串操作
str = '012345678'
print(str)
print(str[0:-1])
print(str[2:3])

# 换行
print("\n")
# raw String
print(r"\n")

# 同一行展示多条语句
import sys

x = 'simple-test'
sys.stdout.write(x + '\n')

# 导出整个模块
import sys
# 从某个模块导入多个函数
from sys import argv, path

print("\n从某个模块导出特定成员 :", path, "\n")

# 基本类型
counter = 100  # 整型
miles = 1000.0  # 浮点型
name = 'String'  # 字符串
print(counter)
print(miles)
print(name)

# 变量赋值
a = b = c = 1
e, d, f = 1, 2, 'str'
print(f)

# 标准数据类型
# Number String bool List Tuple Set Dictionary
d = 3 + 4j  # 复数
print(type(20), type(20.5), type(False), type(d))
print(isinstance(1, int))
print(issubclass(bool, int))

# del 删除对象引用
del d
# print(d,a)  报错


print("\n========== 加减乘除运算 ============")
print(9 / 7)
print(9 // 7)
print(9 % 7)  # 取余
print(2 ** 3)  # 2^3

print("\n========== 列表 ============")

list = ['abcd', 123, 23.3, 3, 4]
nextlist = ['另一个', 123, 'END']
print(list[1:])
print(nextlist * 2)
print(list + nextlist)
print(list[1:4:2])  # 索引1-4,步长为2

print("\n========== 元组 ============")
tuple = ('1', 2, 23.3)
print(tuple)

print("\n========== Set ============")
sites = {'1', '2', 1, '3', '3'}
print(sites)
if '1' in sites:
    print(set('abbc'))
else:
    print(set('bbcddd'))

# a-b 差集; a|b 并集; a&b 交集; a^b 不同时存在的


print("\n========== 字典 ============")
dict = {}
dict['one'] = 'one'
dict[1] = 9

tinydict = {'name': 'panghu', 'age': 18, 4: 5}

print(tinydict.keys())
print(tinydict.values())
print(dict['one'])
print(dict[1])









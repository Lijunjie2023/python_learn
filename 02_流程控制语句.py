# 1.条件判断
# if 条件表达式:
#     代码块
age = 18
if age >= 18:
    print('已成年')

# if else 语句
if age >= 18:
    print('已成年')
else:
    print('未成年')

# if elif else 语句
score = 60
if score >= 90:
    print('优秀')
elif score >= 60:
    print('及格')
else:
    print('不及格')

# 循环
# while 条件表达式:
#     循环体
num = 0
i = 1
while i <= 5:
    num = num + i
    i += 1

print(f"1到5的和是{num}")

# for循环
# range 有三种调用形式：
# range(stop)                 # 生成 0 到 stop-1 的整数
# range(start, stop)          # 生成 start 到 stop-1 的整数
# range(start, stop, step)    # 生成 start 到 stop-1，步长为 step 的整数
for i in range(1, 5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# for遍历字符串
for char in 'hello':
    print(char)

# 遍历字典
person = {"name": "Alice", "age": 25, "city": "北京"}
# 这里可以单独遍历key，value
# 遍历键
for key in person:
    print("key:", key)
    print(key, end=' ')  # name age city
    print()

# 遍历值
for value in person.values():
    print(f"个人信息{value}")

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")
print()

# 循环控制语句
# break continue pass
for i in range(1, 10):
    print(i)
    if (i % 3) == 0:
        break

# continue
print('continue')
for i in range(1, 10):
    if (i % 3) == 0:
        continue
    print(i)

# pass 通常保保障不报错
# 示例1：在if语句中占位
x = 10
if x > 5:
    pass  # 暂时不处理，以后会补充代码
else:
    print("x <= 5")

# 猜数字游戏
import random

target = random.randint(1, 100)
guess = int(input("请输入您猜的数字"))
attempts = 0

while guess != target:
    attempts += 1
    if guess > target:
        print("您猜的数字偏大，请重新输入")
        guess = int(input("请输入您猜的数字"))
    elif guess < target:
        print("您猜的数字偏小，请重新输入")
        guess = int(input("请输入您猜的数字"))
    else:
        print(f"您已猜中，结果为{target}，您用来{attempts}次成功")
attempts += 1
print(f"最后的结果是{target}，您用了{attempts}次成功")

# 在Python中，可以使用 def 关键字来定义函数。函数定义包括函数名称、参数列表和函数体
def greet():
    """这是一个简单的问候函数"""
    print('hello world')


greet()

# 函数内部第一行的字符串常量，用于描述函数功能，可通过 help(函数名) 或 函数名.__doc__ 访问。
print(greet.__doc__)


# 2、参数传递
# 按参数定义的顺序传递，必须提供与函数定义相同数量的参数。
def add(a, b, c):
    print(f"{a}，{b}，{c}之和的结果是{a + b + c}")


add(4, 5, 6)


# 默认参数
def add2(x, y=10):
    print(f"{x},{y}之和的结果是{x + y}")


add2(1)
add2(y=5, x=20)


# 关键字参数
# 调用时可以通过参数名指定，可以不按顺序传递
def introduce(name, age, height):
    print(f"{name},{age},{height}")


introduce(age=18, name="ljj", height=17)

# 可变参数
# *args：接收任意数量的位置参数，打包成元组。
# **kwargs：接收任意数量的关键字参数，打包成字典。
def print_args(*args, **kwargs):
    print("位置参数:", args)
    print("关键字参数:", kwargs)

print_args(1, 2, 3, name="Alice", age=25)

# 函数返回值
def square(num):
    return num * num
print(square(4))

# 变量作用域
# 1、局部变量，在函数内部定义的变量，只在函数内部有效。
# def test():
#     testA  =10
#     print(testA)
# print(testA) 这里会报错

# 全局变量：在函数外部定义的变量，在整个模块中可见。在函数内部可以访问全局变量，但不能直接修改（除非用 global 声明）。
global_var = 100

def read_global():
    print(global_var)   # 可以访问

def modify_global():
    global global_var   # 声明使用全局变量
    global_var = 200    # 修改全局变量

read_global()   # 100
modify_global()
read_global()   # 200

# 运用函数定义、参数和返回值，编写一个简单计算器。
def calculator(a,b,operator = "+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a *b
    elif operator == "/":
        if b==0:
            return "除数不能等于0"
        return a / b

print(calculator(1,2,"-"))
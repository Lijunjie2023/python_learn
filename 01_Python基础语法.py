# 在 Python 中，变量不需要事先声明类型，赋值时自动确定数据类型，这种特性称为动态类型
"""
变量与数据类型
整数 (int)
浮点数 (float)
字符串 (str)
布尔值 (bool)
类型检查与转换
"""

# 整数
a = 10
b = 0b1011
print(a, b)

# 浮点数
pi = 3.1415926
x = 1.5e3
y = 1e-3
z = -0.5
print(pi, x, y, z)

# 字符串
name = 'ljj'
age = 20
email = "ljj163.com"
print(name, age, email)
print(type(name))
print(name[0])
# 截取字符串
sub_str = email[1:3]
print(sub_str)

# 布尔值
is_valid = True
is_empty = False
print(is_valid, is_empty)

# 布尔运算
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# 类型转换和检查
print('类型转换和检查')
var = 3.14
print(type(var))        # <class 'float'>

int_var = int(var)      # 3（截断）
str_var = str(var)      # "3.14"
float_str = float("2.5") # 2.5
bool_val = bool(0)      # False
print(int_var, str_var, float_str, bool_val)

# bmi计算器
print("=== BMI 计算器 ===")
weight = float(input("请输入你的体重（公斤）："))
height = float(input("请输入你的身高（米）："))

bmi = weight / (height ** 2)
print(f"你的 BMI 指数为：{bmi:.2f}")

"""在 Python 的 f-string（格式化字符串字面量）中，{bmi:.2f} 是一个格式化字段，它的含义如下：
bmi：要格式化的变量名（或表达式），假设它是一个浮点数（如 23.456789）。
:：分隔符，后面跟着格式说明符。
.2f：格式说明符，具体含义：
.2 表示小数点后保留 2 位数字。
f 表示将值格式化为定点数（即普通小数，不是科学计数法）。
因此，{bmi:.2f} 的作用是：将变量 bmi 的值四舍五入到小数点后两位，并以字符串形式嵌入到结果中。"""

if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 24:
    print("体重正常")
elif 24 <= bmi < 28:
    print("体重过重")
else:
    print("肥胖")
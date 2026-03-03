import pandas as pd


# 显示所有列
# pandas默认只会显示部分列,中间用省略号 ... 隐藏
pd.set_option('display.max_columns', None)

# print(df)

# 练习题1
# 取出order_detail表里的子订单id、订单id、订单创建时间
'''
导入数据
读取数据
输出数据
'''
# df = pd.read_excel('./订单表.xlsx')
# print(df[['order_id','parent_order_id','create_time']])

# 练习题2
# 取出order_detail表里所有数据
'''
导入数据
读取数据
输出数据
'''
# pd读取的数据是全量的数据
# 列出所有列（太庞大）
# df = pd.read_excel('./订单表.xlsx')
# print(df)

# 练习题3
# 请你根据order_detail表的数据，计算每笔订单的最终优惠金额（平台优惠 + 店铺优惠 + 达人优惠）以及各优惠类型在总优惠金额中的占比，
# 最终输出：子订单id、平台优惠金额、店铺优惠金额、达人优惠金额、总优惠金额、平台优惠金额占比、店铺优惠金额占比、达人优惠金额占比
'''
导入数据
数据读取
计算字段
输出数据
'''
df = pd.read_excel('./订单表.xlsx')

# 计算字段
# 数据清洗通常指处理缺失值、重复值、异常值、格式转换、数据类型转换等
# 需要检查字段类型
df['promotion_shop_amount'] = df['promotion_shop_amount'] / 100
df['promotion_platform_amount'] = df['promotion_platform_amount'] / 100
df['promotion_talent_amount'] = df['promotion_talent_amount'] / 100

# 总优惠计算
df['promotion_total_amount'] = df['promotion_talent_amount'] + df['promotion_shop_amount'] + df['promotion_platform_amount']

df['promotion_shop_rate'] = df['promotion_shop_amount'] / df['promotion_total_amount']
df['promotion_platform_rate'] = df['promotion_platform_amount'] / df['promotion_total_amount']
df['promotion_talent_rate'] = df['promotion_talent_amount'] / df['promotion_total_amount']

# 结果输出
print(df[['order_id','promotion_platform_amount','promotion_shop_amount','promotion_talent_amount','promotion_total_amount','promotion_platform_rate','promotion_shop_rate','promotion_talent_rate',]])
# pandas 中如果分母为0，则结果为inf或NAN（分子也为0）
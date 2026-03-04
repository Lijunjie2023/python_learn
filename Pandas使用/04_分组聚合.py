# 从order_detail表内，计算每笔订单的成交指标，输出：父订单id、订单总金额、成交总金额、平均成交金额、最大成交总金额、优惠金额、购买件数
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
'''
数据导入
数据读取
数据处理
数据分组聚合
数据输出
'''
df = pd.read_excel('./订单表.xlsx')

# 计算字段
df['order_amount'] = df['order_amount'] / 100
df['promotion_shop_amount'] = df['promotion_shop_amount'] / 100
df['promotion_platform_amount'] = df['promotion_platform_amount'] / 100
df['promotion_talent_amount'] = df['promotion_talent_amount'] / 100
df['pay_amount'] = df['pay_amount'] / 100

df['promotion_total_amount'] = df['promotion_shop_amount'] + df['promotion_platform_amount'] + df[
    'promotion_talent_amount']

parent_orders_agg = (df.groupby('parent_order_id')
.agg(
    order_amount=('order_amount', 'sum'),
    pay_amount=('pay_amount', 'sum'),
    pay_amount_avg=('pay_amount', 'mean'),
    pay_anount_max=('pay_amount', 'max'),
    promotion_amount=('promotion_total_amount','sum'),
    item_num=('item_num','sum'),
))

print(parent_orders_agg)


# 从order_detail表内，以创建时间为基准，取出每天数据，输出：日期、商品唯一编码、成交总金额、平均成交金额、最大成交金额、优惠总金额、购买件数
import pandas as pd
'''
数据导入
数据读取
数据分组聚合
数据输出
'''
df = pd.read_excel('./订单表.xlsx')

# 计算字段
df['pay_amount'] = df['pay_amount'] / 100
df['order_amount'] = df['order_amount'] / 100
df['promotion_shop_amount'] = df['promotion_shop_amount'] / 100
df['promotion_platform_amount'] = df['promotion_platform_amount'] / 100
df['promotion_talent_amount'] = df['promotion_talent_amount'] / 100

df['total_promotion_amount'] = df['promotion_shop_amount'] + df['promotion_platform_amount'] + df['promotion_talent_amount']

# 时间转化
# **这里的时间应该要聚合到天，现在拿到的是精确到分钟的时间**
df['dt'] = pd.to_datetime(df['create_time'])

df_agg = df.groupby('dt').agg(
    order_amount=('order_amount', 'sum'),
    order_amount_avg=('order_amount', 'mean'),
    order_amount_max=('order_amount', 'max'),
    promotion_amount=('total_promotion_amount','sum'),
    item_num=('item_num','sum'),
)

df_agg.to_excel('df_agg.xlsx')
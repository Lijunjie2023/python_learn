# 语法df.query('条件')

# 取出order_detail表内，流量来源为「直播间」的子订单id、订单id、作者id、直播id、支付金额

# import pandas as pd
# pd.set_option('display.max_columns', None)
# '''
# 导入数据
# 数据读取
# 数据筛选
# 数据输出
# '''
# df = pd.read_excel('./订单表.xlsx')
#
# df['pay_amount'] = df['pay_amount'] / 100
#
# live_stream_order = df.query('theme_type == 1')
# print(live_stream_order[['order_id','parent_order_id','author_id','room_id','pay_amount']])


# 取出order_detail表内，流量来源为「直播间」且「内容id不为空」的子订单id、订单id、作者id、直播id、支付金额
# import pandas as pd
# pd.set_option('display.max_columns', None)
# '''
# 导入数据
# 读取数据
# 计算字段
# 数据筛选
# 数据输出
# '''
# df = pd.read_excel('./订单表.xlsx')
#
# df['pay_amount'] = df['pay_amount'] / 100
#
# # 这里不等于用!= 表示
# # None 需要用字符串表示
# live_orders = df.query('theme_type == 1' and 'content_id != "None"')
#
# print(live_orders[['order_id','parent_order_id','author_id','room_id','pay_amount']])


# 取出order_detail表内，流量来源为「直播间」或支付类型为「1, 2, 4, 5」的子订单id、订单id、作者id、直播id、支付金额
# import pandas as pd
# '''
# 导入数据
# 读取数据
# 计算字段
# 筛选数据
# 输出数据
# '''
# pd.set_option('display.max_columns', None)
#
# df = pd.read_excel('./订单表.xlsx')
#
# df['pay_amount'] = df['pay_amount'] / 100
#
# live_stream_orders = df.query('theme_type == 1' or 'pay_type in [1,2,4,5]')
#
# print(live_stream_orders[['order_id','parent_order_id','author_id','room_id','pay_amount']])


# 取出order_detail表内，流量来源为「直播间」且订单id中包含「99」并且以「23」结尾的子订单id、订单id、作者id、直播id、支付金额
import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel('./订单表.xlsx')

df['pay_amount'] = df['pay_amount'] / 100

live_stream_orders = df.query('theme_type == 1' and 'order_id.str.contains("99")' and 'order_id.str.endswith("23")' )

print(live_stream_orders[['order_id','parent_order_id','author_id','room_id','pay_amount']])

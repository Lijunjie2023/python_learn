# 取出order_detail表内的支付类型和订单状态，不要重复
import pandas as pd

'''
导入数据
读取数据
数据去重
数据输出
'''

df = pd.read_excel('./订单表.xlsx')
distinct_orders = df.drop_duplicates(subset = ['order_status','pay_type'])
print(distinct_orders[['order_status','pay_type']])
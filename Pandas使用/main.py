import pandas as pd

# pandas
# read_excel()对应的文件需要用字符串包裹，python中路径在编程中就是用字符串表示
df_product = pd.read_excel('./商品信息表.xlsx')
# print(df_product)

# 数据查询 - 取单独列
# 取单独的列：df['列名']
df_product_firstid = df_product['first_cid']
# print(df_product_firstid)

# 取多列 - 用列表包裹
print(df_product[['first_cid','second_cid']])

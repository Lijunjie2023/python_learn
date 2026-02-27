empty_list = []
num_list = [1, 2, 3, 4, 5]
mix_list = [1, 2, 'python', 3]
char = list('python')
print(char)
print(num_list)
print(mix_list)

fruits = ["apple", "banana"]
# 增、删、改、查
# 增
fruits.append("orange")
print(fruits)
fruits.extend(['grap', 'mango'])
print(fruits)
fruits.insert(1, "hhhh")
print(fruits)

# 删
print('删除列表元素')
del fruits[0]
print(fruits)
fruits.remove("banana")
print(fruits)
# pop() 删除并返回指定索引的元素，默认最后一个
last = fruits.pop()
print(last)
print(fruits)

# clear() 清空列表
# fruits.clear()
# print(fruits)  # []

# 查找元素
print('hhhh' in fruits)
print('xxx' in fruits)

print(fruits.index('orange'))
print(fruits.count('orange'))
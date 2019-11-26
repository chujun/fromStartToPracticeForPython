# encoding=utf-8
# sort列表排序
names = ['zhang', 'wang', 'shi', 'chu']
names.sort()
print(names)
# sort列表逆向排序
names.sort(reverse=True)
print(names)
# sorted()函数返回排好序的列表,但不改变原始列表顺序
asc_names = sorted(names)
print(str(names) + "," + str(asc_names))
desc_names = sorted(names, reverse=True)
print(str(names)+","+str(desc_names))

# 反转列表元素
names.append('tian')
names.reverse()
print(names)

# 查询列表长度
print(len(names))
print(names.__len__())

# encoding=utf-8
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0] + "," + bicycles[1])
# 访问最后一个元素[-1],索引-2访问倒数第二个元素 java没有
print(bicycles[-1] + "," + bicycles[-2])
# IndexError: list index out of range
# print(bicycles[-5])
# print(bicycles[4])

bicycles[0] = 'car'
print(bicycles)

ages = []
print(ages)
# 列表尾部添加
ages.append(10)
ages.append(30)
ages.append(45)
print(ages)
# 指定位置添加
ages.insert(0, 1)
print(ages)
# 删除指定位置元素
del ages[-1]
del ages[0]
print(ages)
# 从队尾弹出元素
age = ages.pop()
print(ages.__str__() + "," + str(age))

ages.append(50)
ages.append(60)
ages.append(70)
# 从指定位置弹出元素
age = ages.pop(-2)
print(ages.__str__() + "," + str(age))


age_10 = 10
ages.append(age_10)
# 删除指定值,只会删除第一个满足条件的值,如果没有找到则会抛错
ages.remove(age_10)
print(ages)
# ValueError: list.remove(x): x not in list
# ages.remove(100000)





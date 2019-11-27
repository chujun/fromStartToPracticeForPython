# encoding=utf-8
# 左闭右开
for value in range(1, 5):
    print(value)
# 可以指定步长
for value in range(2, 20, 2):
    print(value)
numbers = range(1, 10)
print(numbers)
print(list(numbers))

suquares = []
suquares = list()
for value in range(1, 11):
    suquares.append(value ** 2)
print(suquares)

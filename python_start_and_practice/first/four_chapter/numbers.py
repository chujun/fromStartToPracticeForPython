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

digits = [1, 2, 3, 4, 5, 6]
print(min(digits))
print(max(digits))
print(sum(digits))
print(min(1, 3, 5, 6))

# 列表解析:一行代码生成平方数列表
suquares = [value ** 2 for value in range(1, 11)]
print(suquares)

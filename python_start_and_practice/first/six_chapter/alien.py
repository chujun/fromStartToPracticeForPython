# encoding=utf-8
alien_0 = {'color': 'green', 'age': 18}
print(alien_0['color'])
print(alien_0['age'])

alien_0['age'] = alien_0['age'] + 1
# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 180
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['age'] = 20
alien_1['x_position'] = 10
alien_1['y_position'] = 80
print(alien_1)

# 删除键
alien_0['test'] = 'test'
print('delete before:' + str(alien_0))
del alien_0['test']
print('delete after:' + str(alien_0))

dic_favorite_laguages = {
    'zhang': 'java',
    'wang': 'C',
    'li': 'C++',
    'zhao': 'Python',
    'shi': 'java',
}
print(dic_favorite_laguages)

# 字典遍历:注意遍历时键值对返回顺序与存储顺序不同
print('------=======--------')
for key, value in dic_favorite_laguages.items():
    print(key + ":" + str(value))
print('------=======--------')
for key in dic_favorite_laguages.keys():
    print(key)
print('------=======--------')
for value in dic_favorite_laguages.values():
    print(str(value))
person_name = 'qian'
if person_name not in dic_favorite_laguages.keys():
    print(person_name + 'not select favorite laguages')

# 按照指定顺序遍历字典
print('------=======--------')
for key in sorted(dic_favorite_laguages.keys()):
    print(key + ":" + dic_favorite_laguages[key])
print('------=======--------')

# set()去除重复项
for value in set(dic_favorite_laguages.values()):
    print(str(value))

# 各种嵌套
aliens = [alien_0, alien_1]
print('------=======--------')
for alien in aliens:
    print(alien)
aliens = []
for number in range(10):
    alien = {'color': 'red', 'age': 18, 'x_position': 20, 'y_position': 40}
    aliens.append(alien)
for alien in aliens[:3]:
    alien['color'] = 'blue'
print('------=======--------')
for alien in aliens[:5]:
    print(alien)

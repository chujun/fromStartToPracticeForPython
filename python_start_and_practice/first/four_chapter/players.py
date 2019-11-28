# encoding=utf-8
players = ['zhang san', 'li si ', 'wang wu', 'zhao liu']
# 获取前两名队员
print(players[0:2])
# 默认从开头开始
print(players[:3])
# 默认到结尾结束
print(players[2:])
print(players[:-1])
print('last 3 players:' + str(players[-3:]))

# 遍历切片
for player in players[:3]:
    print(player)

# 利用列表切片复制整个列表
my_players = players[:]
my_players.append("qian qi")
print('---------=====--------')
for my_player in my_players:
    print(my_player)
print('---------=====--------')
for player in players:
    print(player)

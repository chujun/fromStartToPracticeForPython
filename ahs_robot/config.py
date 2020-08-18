#!/usr/bin/env python
# encoding=utf-8
import configparser
import os

config = configparser.ConfigParser()
env = 'uat'
print(os.getcwd())
# TODO:cj modify ahs_robot
config_file = os.path.join(os.getcwd(), 'config', 'config.%s.ini' % env)
print(config_file)
config.read(config_file, encoding='utf8')
# -sections得到所有的section，并以列表的形式返回
print('sections:', ' ', config.sections())
# -options(section)得到该section的所有option
print('options:', ' ', config.options('base'))
# -items（section）得到该section的所有键值对
print('items:', ' ', config.items('base'))
# -get(section,option)得到section中option的值，返回为string类型
print('get:', ' ', config.getint('base', 'operation_id'))
print('get:', ' ', config.get('base', 'operation_name'))
"""
首先得到配置文件的所有分组，然后根据分组逐一展示所有
"""
for sections in config.sections():
    for items in config.items(sections):
        print(items)

list = config.sections()  # 获取到配置文件中所有分组名称
if 'type' not in list:  # 如果分组type不存在则插入type分组
    config.add_section('type')
    config.set('type', 'stuno', '10211201')  # 给type分组设置值
print(config.sections())
config.remove_option('type', 'stuno')  # 删除type分组的stuno
config.remove_section('type')  # 删除配置文件中type分组
print(config.sections())

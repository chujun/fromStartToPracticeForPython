# coding:utf-8
import os
from multiprocessing.dummy import Pool as ThreadPool

import requests
from lxml import html
import time
import re

# 一些标题中的字符会导致无法创建文件夹
regex = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
# 20190414
url_prefix = 'http://www.mzitu.com/page'
target = 'tmp\\mzitu'


def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': str(referer),
    }
    return headers


def group_urls(page_num):
    base_url = f'{url_prefix}/{page_num}'
    selector = html.fromstring(requests.get(base_url).content)
    urls = []
    # XML Path Language 一种小型的查询语言
    for i in selector.xpath('//ul[@id="pins"]/li/a/@href'):
        urls.append(i)
    return urls


def save(url):
    sel = html.fromstring(requests.get(url).content)
    total = sel.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0]
    title = sel.xpath('//h2[@class="main-title"]/text()')[0]
    title = re.sub(regex, '', title)

    dir_name = f"{os.path.abspath('.')}\\{target}\\【{total}P】{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'{strftime} 开始下载 目录 {dir_name}')

    n = 1
    for i in range(int(total)):
        # 每一页
        try:
            link = f'{url}/{i + 1}'
            s = html.fromstring(requests.get(link).content)
            # 图片地址在src标签中
            jpg_src = s.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
            filename = f'{dir_name}\\{n}.jpg'
            with open(filename, "wb+") as jpg:
                jpg.write(requests.get(
                    jpg_src, headers=header(jpg_src)).content)
            n += 1
        except:
            pass


# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == '__main__':
    start = input(u'请输入起始页码 默认1：')
    try:
        start = int(start)
    except:
        start = 1

    end = input(u'请输入结束页码 默认20：')
    try:
        end = int(end)
    except:
        end = 20
    end = end + 1

    for page in range(start, end):
        pages = group_urls(page)

        # 单线程
        # for p in pages:
        #     save(p)

        # 多线程
        with ThreadPool(4) as pool:
            # map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
            pool.map(save, pages)

    print(u'{} 已完成'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    # save('https://www.mzitu.com/176505')

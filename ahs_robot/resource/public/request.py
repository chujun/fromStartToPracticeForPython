# __*__ coding:utf-8 __*__
# @Author:sharapova

"""
封装requests中post,get,delete,put请求方法
"""
import requests
import json
from resource.public.log import Logger

logger = Logger(logger='RequestLog').getlog()


class RequestMethod(object):
    def __init__(self):
        # requests 配置超时及重试次数
        self.s = requests.Session()

    def run_main(self, method, url, headers=None, data=None):
        # requests.adapters.DEFAULT_RETRIES = 5
        # 根据请求方式指定入参
        methods = {'POST': self.s.post,
                   'GET': self.s.get,
                   'DELETE': self.s.delete,
                   'PUT': self.s.put}
        if method not in methods.keys():
            error_info = "%s接口%s方法暂时不支持" % (url, method)
            logger.error(error_info)
            raise ValueError(error_info)
        json_data = None
        if data is not None:
            json_data = json.dumps(data)
        res = methods[method](url=url, headers=headers, data=json_data, timeout=5, verify=False)
        logger.info("%s接口%s方法请求结果==》%s " % (url, method, res.text))
        return res


if __name__ == '__main__':
    request = RequestMethod()
    res = request.run_main('GET', 'http://www.baidu.com')

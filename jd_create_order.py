# __*__ coding:utf-8 __*__
# @Author:sharapova
from hashlib import sha1
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import requests, time,json

unpad = lambda s: s[0:-ord(s[-1])]


def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# sha1加密
def mySha1(string):
    sh = sha1()
    sh.update(string.encode('utf-8'))
    return sh.hexdigest()


# 生成url时间戳和token
def getQueryString():
    timestamp = str(int(round(time.time() * 1000)))
    print(timestamp)
    string = "7.huishou.jd.com"
    sign = string + timestamp + string
    queryString = '?timestamp=' + timestamp + '&token=' + mySha1(sign)
    # print(queryString)
    return queryString


# aes加密
def aes_encrypt(key, aes_str):
    # 使用key,选择加密方式
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')  # 选择pkcs7补全
    encrypt_aes = aes.encrypt(pad_pkcs7)
    # 加密结果
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    encrypted_text_str = encrypted_text.replace("\n", "")
    return encrypted_text_str


# 解密
def aes_decrypt(key, text):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypted_text = unpad(aes.decrypt(base64_decrypted).decode('utf-8'))
    decrypted_code = decrypted_text.rstrip('\0')
    # print(decrypted_code)
    return decrypted_code


def create_order(jdrecycleOrderNo):
    """
    创建订单
    :return:
    """
    url = 'http://47.96.53.33:8080/cooperator-openapi/jd/one-stop/create-order' + getQueryString()
    data = '{"couponAmount":0,"inquiryKey":"1284609983606239902","onDoorInfo":{"pickDate":1573574400000},"paidAmount":7869.0,"pickupType":1,"prePayAmount":2760,"receiverInfo":{"address":"科创十一街18号京东大厦C座16层","cityId":2810,"cityName":"大兴区","countyId":51081,"countyName":"亦庄经济开发区","provinceId":1,"provinceName":"北京"},"recycleOrderNo":' + str(
        jdrecycleOrderNo) + ',"saleOrderNo":"106207521157","salePrice":9599.0,"stationInfo":{"id":848788,"name":"北京力宝华联爱回收合作站"},"subsidyAmount":0,"subsidyRule":"","userMobile":"18221413949","userName":"yytest","userPin":"ZKhuQf8uj5gKx9qAgALdtA=="}'
    header = {'Content-Type': 'application/json'}
    res = requests.post(url, data=aes_encrypt('7.huishou.jd.com', data), headers=header)
    print(res.text)
    print(aes_decrypt('7.huishou.jd.com', res.text))


def split_order(jdrecycleOrderNo, saleOrderNo):
    """
    拆单
    :param jdrecycleOrderNo:
    :param saleOrderNo:
    :return:
    """
    url = 'http://47.96.53.33:8080/cooperator-openapi/jd/one-stop/split-order' + getQueryString()
    data = '{"childOrders":[],"isSplit":false,"recycleOrderNo":' + str(jdrecycleOrderNo) + ',"saleOrderNo":' + str(
        saleOrderNo) + '}'
    print(data)
    print(aes_encrypt('7.huishou.jd.com', data))
    header = {'Content-Type': 'application/json'}
    res = requests.post(url, data=aes_encrypt('7.huishou.jd.com', data), headers=header)
    print(res.text)
    print(aes_decrypt('7.huishou.jd.com', res.text))


def deliver(jdrecycleOrderNo, saleOrderNo, logisticNo):
    """
    创建取件单
    :param jdrecycleOrderNo:
    :param saleOrderNo:
    :param logisticNo:
    :return:
    """
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    url = 'http://47.96.53.33:8080/cooperator-openapi/jd/one-stop/deliver' + getQueryString()
    body = {"createdAt":nowTime,"isSplit":False,"logisticNo":logisticNo,"recycleOrderNo":jdrecycleOrderNo,"saleOrderNo":saleOrderNo}
    data1 = json.dumps(body)
    data = str(data1)
    print(aes_encrypt('7.huishou.jd.com', data))
    header = {'Content-Type': 'application/json'}
    res = requests.post(url, data=aes_encrypt('7.huishou.jd.com', data), headers=header)
    print(res.text)
    print(aes_decrypt('7.huishou.jd.com', res.text))


if __name__ == '__main__':
    jdrecycleOrderNo = 14431666
    saleOrderNo = 106379889874
    logisticNo = 106379889874
    # create_order(jdrecycleOrderNo)
    # split_order(jdrecycleOrderNo, saleOrderNo)
    deliver(jdrecycleOrderNo, saleOrderNo, logisticNo)


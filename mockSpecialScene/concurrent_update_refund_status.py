# encoding=utf-8
import requests
import threading
import time

success_code = 200


def post(url, jsonData=None, header=None):
    if not header:
        header = {'Content-Type': 'application/json'}
    print_time(str(header) + "," + str(jsonData))
    response = requests.post(url, json=jsonData, headers=header)
    validate(response)


def validate(response):
    if not response:
        raise RuntimeError('not exist response')
    response.raise_for_status()  # 如果状态不是200，则引发异常
    if not response.content:
        raise RuntimeError('response not exist content')
    # print_time(response)
    dist_data = response.json()
    if dist_data['code'] != success_code:
        print_time('warning:not success')
    data = str(response.content, encoding="utf-8")
    print_time(data)


domain_url = 'http://localhost:8080'
tic_service_url = domain_url + "/trade-in-center"
receipt_notify_url = tic_service_url + "/receipt/trade-in-order/notify/"
update_refund_status_url = tic_service_url + "/int/trade-in-order/refund-transaction/{0}/update-status"
update_refund_status_by_out_serial_no_url = \
    tic_service_url + "/int/trade-in-order/refund-transaction/out-serial-no/{0}/update-status"

receipt_status_enum = {
    'success': 7
}


class NotifyThread(threading.Thread):
    def __init__(self, thread_id, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = 'notify_thread'
        self.counter = counter

    def run(self):
        print_time("开始线程：" + self.name)
        mock_receipt_notify_refund_success()
        print_time("退出线程：" + self.name)


class UpdateStatusThread(threading.Thread):
    def __init__(self, thread_id, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = 'update_status_thread'
        self.counter = counter

    def run(self):
        print_time("开始线程：" + self.name)
        for count in range(0, self.counter):
            print_time("开始循环调用mock_update_refund_transaction_status_by_out_serial_no" + str(count))
            mock_update_refund_transaction_status_by_out_serial_no()
        print_time("退出线程：" + self.name)


def mock_receipt_notify_refund_success():
    out_serial_no = '201912061718389392190201000'
    post(receipt_notify_url, {"receiptBill": {"outSerialNo": out_serial_no, "status": receipt_status_enum['success']}})


def mock_update_refund_transaction_status():
    trade_in_order_refund_transaction_id = 186
    post(update_refund_status_url.format(str(trade_in_order_refund_transaction_id)))


def mock_update_refund_transaction_status_by_out_serial_no():
    out_serial_no = '201912061718389392190201000'
    post(update_refund_status_by_out_serial_no_url.format(str(out_serial_no)))


def print_time(string):
    print(str(time.time()) + ":" + str(string))


if __name__ == '__main__':
    print_time('start script:')
    # mock_receipt_notify_refund_success()
    # mock_update_refund_transaction_status()
    # 创建新线程
    thread1 = NotifyThread(1, 1)
    thread1.start()
    for t in range(0, 4):
        thread2 = UpdateStatusThread(2, 10)
        thread2.start()
    # 开启新线程

    thread1.join()

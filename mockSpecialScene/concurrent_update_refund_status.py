# encoding=utf-8
import requests
import json


def post(url, jsonData=None, header=None):
    if not header:
        header = {'Content-Type': 'application/json'}
    print(str(header) + "," + str(jsonData))
    response = requests.post(url, json=jsonData, headers=header)
    validate(response)


success_code = 200


def validate(response):
    if not response:
        raise RuntimeError('not exist response')
    response.raise_for_status()  # 如果状态不是200，则引发异常
    if not response.content:
        raise RuntimeError('response not exist content')
    print(response)
    dist_data = response.json()
    if dist_data['code'] != success_code:
        raise RuntimeError('response code error' + str(dist_data))
    data = str(response.content, encoding="utf-8")
    print(data)


domain_url = 'http://localhost:8080'
tic_service_url = domain_url + "/trade-in-center"
receipt_notify_url = tic_service_url + "/receipt/trade-in-order/notify/"
update_refund_status_url = tic_service_url + "/int/trade-in-order/refund-transaction/{0}/update-status"

receipt_status_enum = {
    'success': 8
}


def mock_receipt_notify_refund_success(out_serial_no):
    post(receipt_notify_url, {"receiptBill": {"outSerialNo": out_serial_no, "status": receipt_status_enum['success']}})


def mock_update_refund_transaction_status(trade_in_order_refund_transaction_id):
    post(update_refund_status_url.format(str(trade_in_order_refund_transaction_id)))


if __name__ == '__main__':
    print('start script:')
    out_serial_no = '20190124155711508364091010'
    trade_in_order_refund_transaction_id = 155
    mock_receipt_notify_refund_success(out_serial_no)
    mock_update_refund_transaction_status(trade_in_order_refund_transaction_id)

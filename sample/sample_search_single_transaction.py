# -*- coding: utf-8 -*-

import importlib.util
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk",
    "/path/to/ecpay_payment_sdk.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

import time
import pprint
from datetime import datetime

search_single_transaction_params = {
    'CreditRefundId': 10123456,  # 信用卡授權單號
    'CreditAmount': 100,  # 金額
    'CreditCheckCode': 59997889,  # 商家檢查碼
}

# 建立實體
ecpay_payment_sdk = module.ECPayPaymentSdk(
    MerchantID='3002607',
    HashKey='pwFHCqoQZGmho4w6',
    HashIV='EkRm7iFT261dpevs'
)

try:
    # 介接路徑
    # query_url = '因無法提供實際授權，故無法使用此API' # 測試環境
    query_url = 'https://payment.ecPay.com.tw/CreditDetail/QueryTrade/V2'  # 正式環境

    # 查詢訂單
    query_result = ecpay_payment_sdk.search_single_transaction(
        client_parameters=search_single_transaction_params)
    pprint.pprint(query_result)

except Exception as error:
    print('An exception happened: ' + str(error))

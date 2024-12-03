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

download_disbursement_balance_params = {
    'PayDateType': 'close',
    'StartDate': '2018-02-12',  # 日期格式為「yyyy-MM-dd」, ex: 2017-02-12
    'EndDate': '2018-02-12',  # 日期格式為「yyyy-MM-dd」, ex: 2017-02-12
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
    query_url = 'https://payment.ecPay.com.tw/CreditDetail/FundingReconDetail'  # 正式環境

    # 查詢訂單
    query_result = ecpay_payment_sdk.download_disbursement_balance(
        client_parameters=download_disbursement_balance_params)
    print(query_result)

except Exception as error:
    print('An exception happened: ' + str(error))

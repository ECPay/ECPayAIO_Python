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

order_search_params = {
    'MerchantTradeNo': 'kncs20180804103309',
    'TimeStamp': int(time.time())
}

# 建立實體
ecpay_payment_sdk = module.ECPayPaymentSdk(
    MerchantID='2000132',
    HashKey='5294y06JbISpM5x9',
    HashIV='v77hoKGq4kWxNNIS'
)

try:
    # 介接路徑
    query_url = 'https://payment-stage.ecpay.com.tw/Cashier/QueryTradeInfo/V5'  # 測試環境
    # query_url = 'https://payment.ecpay.com.tw/Cashier/QueryTradeInfo/V5' # 正式環境

    # 查詢訂單
    query_result = ecpay_payment_sdk.order_search(
        action_url=query_url,
        client_parameters=order_search_params)
    pprint.pprint(query_result)

except Exception as error:
    print('An exception happened: ' + str(error))

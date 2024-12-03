# -*- coding: utf-8 -*-

import importlib.util
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk",
    "/path/to/ecpay_payment_sdk.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
import pprint

credit_do_action_params = {
    'MerchantTradeNo': '特店交易編號',
    'TradeNo': '綠界的交易編號', # ECpay 的交易編號
    'Action': 'C', # 執行動作
    'TotalAmount': 100,
    'PlatformID': '',
}

# 建立實體
ecpay_payment_sdk = module.ECPayPaymentSdk(
    MerchantID='3002607',
    HashKey='pwFHCqoQZGmho4w6',
    HashIV='EkRm7iFT261dpevs'
)

try:
    # 介接路徑
    #query_url = '因無法提供實際授權，故無法使用此API'  # 測試環境
    query_url = 'https://payment.ecpay.com.tw/CreditDetail/DoAction' # 正式環境

    # 查詢訂單
    query_result = ecpay_payment_sdk.credit_do_action(
        client_parameters=credit_do_action_params)
    pprint.pprint(query_result)

except Exception as error:
    print('An exception happened: ' + str(error))

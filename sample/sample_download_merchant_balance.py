# -*- coding: utf-8 -*-

import importlib.util
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk",
    "/path/to/ecpay_payment_sdk.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

download_merchant_balance_params = {
    'DateType': '6',
    'BeginDate': '2018-02-12', # 日期格式為「yyyy-MM-dd」, ex: 2017-02-12
    'EndDate': '2018-02-12', # 日期格式為「yyyy-MM-dd」, ex: 2017-02-12
    'PaymentType': '01',
    'PlatformStatus': '2',
    'PaymentStatus': '1',
    'AllocateStatus': '0',
    'MediaFormated': '1',
}

# 建立實體
ecpay_payment_sdk = module.ECPayPaymentSdk(
    MerchantID='2000132',
    HashKey='5294y06JbISpM5x9',
    HashIV='v77hoKGq4kWxNNIS'
)

try:
    # 介接路徑
    action_url = 'https://vendor-stage.ecpay.com.tw/PaymentMedia/TradeNoAio' # 測試環境
    # action_url = 'https://vendor.ecpay.com.tw/PaymentMedia/TradeNoAio' # 正式環境

    # 查詢訂單
    query_result = ecpay_payment_sdk.download_merchant_balance(
        action_url=action_url,
        client_parameters=download_merchant_balance_params)
    print(query_result)

except Exception as error:
    print('An exception happened: ' + str(error))

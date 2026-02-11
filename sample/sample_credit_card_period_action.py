# -*- coding: utf-8 -*-
# 信用卡定期定額訂單作業 (補授權 ReAuth / 終止 Cancel)
# 參考 https://developers.ecpay.com.tw/2900.md
# API 路徑: /Cashier/CreditCardPeriodAction
# Action: ReAuth (補授權失敗交易) / Cancel (終止定期定額後續交易)
# 注意：
# - ReAuth 限當筆交易最新一筆授權失敗時才能使用
# - Cancel 終止交易成功後無法重新啟用
# - Stage 測試環境無法測試 ReAuth

import importlib.util
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk",
    "/path/to/ecpay_payment_sdk.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
import time
import pprint

credit_card_period_action_params = {
    'MerchantTradeNo': '特店交易編號',  # 訂單產生時傳送給綠界的特店交易編號
    'Action': 'Cancel',  # ReAuth: 補授權失敗交易 / Cancel: 終止定期定額後續交易
    'TimeStamp': int(time.time()),
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
    query_url = 'https://payment-stage.ecpay.com.tw/Cashier/CreditCardPeriodAction'  # 測試環境
    # query_url = 'https://payment.ecpay.com.tw/Cashier/CreditCardPeriodAction' # 正式環境

    # 執行定期定額訂單作業
    query_result = ecpay_payment_sdk.credit_card_period_action(
        action_url=query_url,
        client_parameters=credit_card_period_action_params)
    pprint.pprint(query_result)

except Exception as error:
    print('An exception happened: ' + str(error))

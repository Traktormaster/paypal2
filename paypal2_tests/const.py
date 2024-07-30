from pydantic import BaseModel


class ConstRequestData(BaseModel):
    body: bytes
    headers: dict[str, str]


HOOK_CERTS = {
    "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb": b"-----BEGIN CERTIFICATE-----\r\nMIIHXDCCBkSgAwIBAgIQA/ujbySX3tuj46W/d7zhxDANBgkqhkiG9w0BAQsFADB1\r\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\r\nd3cuZGlnaWNlcnQuY29tMTQwMgYDVQQDEytEaWdpQ2VydCBTSEEyIEV4dGVuZGVk\r\nIFZhbGlkYXRpb24gU2VydmVyIENBMB4XDTI0MDMwODAwMDAwMFoXDTI1MDMwNzIz\r\nNTk1OVowgdsxEzARBgsrBgEEAYI3PAIBAxMCVVMxGTAXBgsrBgEEAYI3PAIBAhMI\r\nRGVsYXdhcmUxHTAbBgNVBA8MFFByaXZhdGUgT3JnYW5pemF0aW9uMRAwDgYDVQQF\r\nEwczMDE0MjY3MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTERMA8G\r\nA1UEBxMIU2FuIEpvc2UxFTATBgNVBAoTDFBheVBhbCwgSW5jLjEsMCoGA1UEAxMj\r\nbWVzc2FnZXZlcmlmaWNhdGlvbmNlcnRzLnBheXBhbC5jb20wggEiMA0GCSqGSIb3\r\nDQEBAQUAA4IBDwAwggEKAoIBAQC4GzoXbAbZY1nNrR6sr/WGBKHrv5MzXK+QY2lt\r\nN0eZFSMR3Q/FhTSVKyFGEtqpdkVu2RwnJnpz0dtDAnssBZTDE/3dafGT41cPPtjQ\r\nTx/VLhC0noV+SCcwYk2Bv7vm2RqeJUUVqThouNmZPaRZNpMPQDAqdHUoIxSk/kQl\r\nhPVHhTCpjY9wwUbwn49E/+f44W87kkeXsrbTet6bSeqgW1oy7sj2QR0vg2xi1yYy\r\ndNqhMhsceh3pV7qRfvlP7Rv3yorsCWZXAbxSB7MKzcSsnM2n4iE20pTWWiUaKLPI\r\nL4vTqfl0cqRygKx0Pcy4aknxIRwbI8Ab493j5c2Rmtxv4ZJhAgMBAAGjggN/MIID\r\nezAfBgNVHSMEGDAWgBQ901Cl1qCt7vNKYApl0yHU+PjWDzAdBgNVHQ4EFgQUGTJR\r\nHgzRoA4BYXr5GPWiwCf5gd8wLgYDVR0RBCcwJYIjbWVzc2FnZXZlcmlmaWNhdGlv\r\nbmNlcnRzLnBheXBhbC5jb20wSgYDVR0gBEMwQTALBglghkgBhv1sAgEwMgYFZ4EM\r\nAQEwKTAnBggrBgEFBQcCARYbaHR0cDovL3d3dy5kaWdpY2VydC5jb20vQ1BTMA4G\r\nA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwdQYD\r\nVR0fBG4wbDA0oDKgMIYuaHR0cDovL2NybDMuZGlnaWNlcnQuY29tL3NoYTItZXYt\r\nc2VydmVyLWczLmNybDA0oDKgMIYuaHR0cDovL2NybDQuZGlnaWNlcnQuY29tL3No\r\nYTItZXYtc2VydmVyLWczLmNybDCBiAYIKwYBBQUHAQEEfDB6MCQGCCsGAQUFBzAB\r\nhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wUgYIKwYBBQUHMAKGRmh0dHA6Ly9j\r\nYWNlcnRzLmRpZ2ljZXJ0LmNvbS9EaWdpQ2VydFNIQTJFeHRlbmRlZFZhbGlkYXRp\r\nb25TZXJ2ZXJDQS5jcnQwDAYDVR0TAQH/BAIwADCCAXwGCisGAQQB1nkCBAIEggFs\r\nBIIBaAFmAHUATnWjJ1yaEMM4W2zU3z9S6x3w4I4bjWnAsfpksWKaOd8AAAGOHuxW\r\nNwAABAMARjBEAiA794gDwBlLuPrnv5Fj4ablrQ0rdN79WXYKElFRlZfFwQIgbSkU\r\n2m9OuKVbhYkYye2p7uEZaY+7CIau2CgGn021hb4AdgB9WR4S4XgqexxhZ3xe/fjQ\r\nh1wUoE6VnrkDL9kOjC55uAAAAY4e7FX0AAAEAwBHMEUCIH/TXkK2Wg7UAa1E0G0A\r\nBP2PZubHPXyzhtWUQWo0S7SyAiEAuKaUmmoOH7eS+cZXu18EwdU0b0/Fr4vTIeAW\r\ndBwuOOQAdQDm0jFjQHeMwRBBBtdxuc7B0kD2loSG+7qHMh39HjeOUAAAAY4e7FYQ\r\nAAAEAwBGMEQCIFsrE/dHNM1QbIclR/50AiCNtoKjcGJFoblgaVnWW/6uAiBA5EE+\r\nvX1dxUdluf6cktPuo0IxYZSd6WCG4zqBMR292TANBgkqhkiG9w0BAQsFAAOCAQEA\r\nvKdi82U0vGaCCAYN598wEN6Ktu+BeZp3W3p1iVRBZgY9l0JPjwWN8Apwm4BUUTp3\r\n00gpIfROKvyR1655B0QDv/oL1Wuz/zQ87kUGVZNNeac07+X2e6YP5sqrwF4ttWai\r\najFRa8M2Y6vEk+7EmSexynxJBRa86Aa4xogqlTv/7kXf7LrDzMTlfle7o2L7eqwd\r\nCIc7vCYw9XQ5K80d4Siy6xz+RSu7+Un8QlfAYB7z1o32uPEUihk05ulMiXJYvA0W\r\nOagItBsuMSzgwQ0KDC9EmDYmXE9xWtUolehmBGRyQw+/E7iVu4x4js1HRiD0M+s9\r\nbRQ14PLxRLqDKu8oqZ8DQA==\r\n-----END CERTIFICATE-----",
}

HOOK_SUBSCRIPTION_CREATED_v2_0 = ConstRequestData(
    body=b'{"id":"WH-TY567577T725889R5-1E6T55435R66166TR","create_time":"2018-19-12T22:20:32.000Z","event_type":"BILLING.SUBSCRIPTION.CREATED","event_version":"1.0","resource_type":"subscription","resource_version":"2.0","summary":"A billing subscription was created.","resource":{"id":"I-BW452GLLEP1G","status":"APPROVAL_PENDING","status_update_time":"2018-12-10T21:20:49Z","plan_id":"P-5ML4271244454362WXNWU5NQ","start_time":"2018-11-01T00:00:00Z","quantity":"20","shipping_amount":{"currency_code":"USD","value":"10.00"},"subscriber":{"name":{"given_name":"John","surname":"Doe"},"email_address":"customer@example.com","shipping_address":{"name":{"full_name":"John Doe"},"address":{"address_line_1":"2211 N First Street","address_line_2":"Building 17","admin_area_2":"San Jose","admin_area_1":"CA","postal_code":"95131","country_code":"US"}}},"auto_renewal":true,"billing_info":{"outstanding_balance":{"currency_code":"USD","value":"10.00"},"cycle_executions":[{"tenure_type":"TRIAL","sequence":1,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1},{"tenure_type":"REGULAR","sequence":2,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1}],"last_payment":{"amount":{"currency_code":"USD","value":"500.00"},"time":"2018-12-01T01:20:49Z"},"next_billing_time":"2019-01-01T00:20:49Z","final_payment_time":"2020-01-01T00:20:49Z","failed_payments_count":2},"create_time":"2018-12-10T21:20:49Z","update_time":"2018-12-10T21:20:49Z","links":[{"href":"https://www.paypal.com/webapps/billing/subscriptions?ba_token=BA-4GH39689T3856352J","rel":"approve","method":"GET"},{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G","rel":"edit","method":"PATCH"},{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G/activate","rel":"activate","method":"POST"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/TY567577T725889R5-1E6T55435R66166TR","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-TY567577T725889R5-1E6T55435R66166TR/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "2212",
        "accept": "*/*",
        "paypal-transmission-id": "b5eb01d0-4e5c-11ef-8572-997c8c58ed96",
        "paypal-transmission-time": "2024-07-30T10:15:56Z",
        "paypal-transmission-sig": "grQeWT9st61L2Qrf4GoL/j6LTbiRiRiQgoOvwkC4jGIbeQFE/EUdQq0vUIfn+kg7KqRk2wGdWDs9G+dd8F4GSE/WYiTOnN1a7NuojW2yZ06jGgWImo8yyJrhtK55BsU+bRolgPvBgXL6Iu33+gPjsY2F1tWSMco5wjJiDtQ6kDb1pS8HWkoH+caOoKibJw8ZdBRrNTc9OZ/Y3Dt9zVkElNA05Lf+wvJk9rF5fD6XAAA+ZdyKYY7+srfbsgZZDtQ5SaaMBg9fPnd6E7pTM6/eYWB9IVEWYnbWNEc37Y+irR12jjaOA4d8DwmRa0q4z7ajQ/emUw0B4zxee/eTpkeppQ==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "a4c89ebb5e90f",
        "x-b3-spanid": "575d15fa3cb9fbc2",
    },
)
HOOK_PAYMENT_SALE_COMPLETED = ConstRequestData(
    body=b'{"id":"WH-2WR32451HC0233532-67976317FL4543714","event_version":"1.0","create_time":"2014-10-23T17:23:52Z","resource_type":"sale","event_type":"PAYMENT.SALE.COMPLETED","summary":"A successful sale payment was made for $ 0.48 USD","resource":{"id":"80021663DE681814L","create_time":"2014-10-23T17:22:56Z","update_time":"2014-10-23T17:23:04Z","amount":{"total":"0.48","currency":"USD"},"payment_mode":"ECHECK","state":"completed","protection_eligibility":"ELIGIBLE","protection_eligibility_type":"ITEM_NOT_RECEIVED_ELIGIBLE,UNAUTHORIZED_PAYMENT_ELIGIBLE","clearing_time":"2014-10-30T07:00:00Z","parent_payment":"PAY-1PA12106FU478450MKRETS4A","links":[{"href":"https://api.paypal.com/v1/payments/sale/80021663DE681814L","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/payments/sale/80021663DE681814L/refund","rel":"refund","method":"POST"},{"href":"https://api.paypal.com/v1/payments/payment/PAY-1PA12106FU478450MKRETS4A","rel":"parent_payment","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-2WR32451HC0233532-67976317FL4543714","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-2WR32451HC0233532-67976317FL4543714/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1263",
        "accept": "*/*",
        "paypal-transmission-id": "8ad71ae0-4e5e-11ef-b16d-8fad525a7f7b",
        "paypal-transmission-time": "2024-07-30T10:29:03Z",
        "paypal-transmission-sig": "MOKfu0nT75NZoa5+Zq3Bxx/vs4TZfd6aVje6+F3fE4cBM1BcdRGmABTj/hJ4yPY0q8QxRjo6e2/PK22Tle4XxjPjoBnMigmbQP/bay3QfYKf12e1HGuZjtJ5kQX+kweY+QhnLmTv2vIuLXAAeLqcg07hs7pZgFP/K2otxG58enQ0HM/WER2+klpfFLViVE6tzBksbMGtRmykfXqO592GEpgvdeshX3MdabgMYnfrT2+ttgRmpo1DvbZ6z0TWPhQ487y4ZH/aR6yQfXTNwta43CNHjKRxc/PrY1pQ8KXDpBafrsnyxygH+98vW8L0zIO2c7kUMa4ZY+OnhfPayaWT5Q==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "2fc7dab820bcc",
        "x-b3-spanid": "9b5d087106470e95",
    },
)


HOOK_SUBSCRIPTION_CREATED_v1_0 = ConstRequestData(  # NOTE: older api version, not used for our system
    body=b'{"id":"WH-19973937YW279670F-02S63370HL636500Y","event_version":"1.0","create_time":"2016-04-28T11:29:31Z","resource_type":"Agreement","event_type":"BILLING.SUBSCRIPTION.CREATED","summary":"A billing subscription was created","resource":{"id":"I-PE7JWXKGVN0R","shipping_address":{"recipient_name":"Cool Buyer","line1":"3rd st","line2":"cool","city":"San Jose","state":"CA","postal_code":"95112","country_code":"US"},"plan":{"curr_code":"USD","links":[],"payment_definitions":[{"type":"TRIAL","frequency":"Month","frequency_interval":"1","amount":{"value":"5.00"},"cycles":"5","charge_models":[{"type":"TAX","amount":{"value":"1.00"}},{"type":"SHIPPING","amount":{"value":"1.00"}}]},{"type":"REGULAR","frequency":"Month","frequency_interval":"1","amount":{"value":"10.00"},"cycles":"15","charge_models":[{"type":"TAX","amount":{"value":"2.00"}},{"type":"SHIPPING","amount":{"value":"1.00"}}]}],"merchant_preferences":{"setup_fee":{"value":"0.00"},"auto_bill_amount":"YES","max_fail_attempts":"21"}},"payer":{"payment_method":"paypal","status":"verified","payer_info":{"email":"coolbuyer@example.com","first_name":"Cool","last_name":"Buyer","payer_id":"XLHKRXRA4H7QY","shipping_address":{"recipient_name":"Cool Buyer","line1":"3rd st","line2":"cool","city":"San Jose","state":"CA","postal_code":"95112","country_code":"US"}}},"agreement_details":{"outstanding_balance":{"value":"0.00"},"num_cycles_remaining":"5","num_cycles_completed":"0","final_payment_due_date":"2017-11-30T10:00:00Z","failed_payment_count":"0"},"description":"desc","state":"Pending","links":[{"href":"https://api.paypal.com/v1/payments/billing-agreements/I-PE7JWXKGVN0R","rel":"self","method":"GET"}],"start_date":"2016-04-30T07:00:00Z"},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-19973937YW279670F-02S63370HL636500Y","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-19973937YW279670F-02S63370HL636500Y/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1995",
        "accept": "*/*",
        "paypal-transmission-id": "337cac50-4e55-11ef-929c-63996ea1b880",
        "paypal-transmission-time": "2024-07-30T09:22:11Z",
        "paypal-transmission-sig": "XnXpPq6CxTx4xY8WNGOnBwSvmLWKf5ZdxnWWQ/2EnIC0Y8Tsn7kSPfGWNkBXq62FpPUmyuIvHRawCYpHCWBVp/RPQDcwLjrlr+VRr952EUMoYXFr9GIc0oXlLhNzIJlC/yn6hyr38q3qVNEDv1IVgdKZ16qKVrwQJ4hm55ruFeO7YSxgX0quU/H8AdcIg2GDGrMJQwFwzGDslCgu1txCz+5Ly2iCQq5r2guSm+kzTXQxR9LTxNZJjAGm7qarHYuKN+d3feHto3yaTesupoO6efBgAyr8p3zqgJODBrrrfzAmHIqd+YX5LogmxW9ErSGwk4mLFcICR+lbc4Xo2WAZVw==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "6029b4a2cc5af",
        "x-b3-spanid": "d4a46f423fa15f1",
    },
)

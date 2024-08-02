"""
Simulated WebHook messages for reference.
"""

from pydantic import BaseModel


class ConstRequestData(BaseModel):
    body: bytes
    headers: dict[str, str]


HOOK_CERTS = {
    "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb": b"-----BEGIN CERTIFICATE-----\r\nMIIHXDCCBkSgAwIBAgIQA/ujbySX3tuj46W/d7zhxDANBgkqhkiG9w0BAQsFADB1\r\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\r\nd3cuZGlnaWNlcnQuY29tMTQwMgYDVQQDEytEaWdpQ2VydCBTSEEyIEV4dGVuZGVk\r\nIFZhbGlkYXRpb24gU2VydmVyIENBMB4XDTI0MDMwODAwMDAwMFoXDTI1MDMwNzIz\r\nNTk1OVowgdsxEzARBgsrBgEEAYI3PAIBAxMCVVMxGTAXBgsrBgEEAYI3PAIBAhMI\r\nRGVsYXdhcmUxHTAbBgNVBA8MFFByaXZhdGUgT3JnYW5pemF0aW9uMRAwDgYDVQQF\r\nEwczMDE0MjY3MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTERMA8G\r\nA1UEBxMIU2FuIEpvc2UxFTATBgNVBAoTDFBheVBhbCwgSW5jLjEsMCoGA1UEAxMj\r\nbWVzc2FnZXZlcmlmaWNhdGlvbmNlcnRzLnBheXBhbC5jb20wggEiMA0GCSqGSIb3\r\nDQEBAQUAA4IBDwAwggEKAoIBAQC4GzoXbAbZY1nNrR6sr/WGBKHrv5MzXK+QY2lt\r\nN0eZFSMR3Q/FhTSVKyFGEtqpdkVu2RwnJnpz0dtDAnssBZTDE/3dafGT41cPPtjQ\r\nTx/VLhC0noV+SCcwYk2Bv7vm2RqeJUUVqThouNmZPaRZNpMPQDAqdHUoIxSk/kQl\r\nhPVHhTCpjY9wwUbwn49E/+f44W87kkeXsrbTet6bSeqgW1oy7sj2QR0vg2xi1yYy\r\ndNqhMhsceh3pV7qRfvlP7Rv3yorsCWZXAbxSB7MKzcSsnM2n4iE20pTWWiUaKLPI\r\nL4vTqfl0cqRygKx0Pcy4aknxIRwbI8Ab493j5c2Rmtxv4ZJhAgMBAAGjggN/MIID\r\nezAfBgNVHSMEGDAWgBQ901Cl1qCt7vNKYApl0yHU+PjWDzAdBgNVHQ4EFgQUGTJR\r\nHgzRoA4BYXr5GPWiwCf5gd8wLgYDVR0RBCcwJYIjbWVzc2FnZXZlcmlmaWNhdGlv\r\nbmNlcnRzLnBheXBhbC5jb20wSgYDVR0gBEMwQTALBglghkgBhv1sAgEwMgYFZ4EM\r\nAQEwKTAnBggrBgEFBQcCARYbaHR0cDovL3d3dy5kaWdpY2VydC5jb20vQ1BTMA4G\r\nA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwdQYD\r\nVR0fBG4wbDA0oDKgMIYuaHR0cDovL2NybDMuZGlnaWNlcnQuY29tL3NoYTItZXYt\r\nc2VydmVyLWczLmNybDA0oDKgMIYuaHR0cDovL2NybDQuZGlnaWNlcnQuY29tL3No\r\nYTItZXYtc2VydmVyLWczLmNybDCBiAYIKwYBBQUHAQEEfDB6MCQGCCsGAQUFBzAB\r\nhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wUgYIKwYBBQUHMAKGRmh0dHA6Ly9j\r\nYWNlcnRzLmRpZ2ljZXJ0LmNvbS9EaWdpQ2VydFNIQTJFeHRlbmRlZFZhbGlkYXRp\r\nb25TZXJ2ZXJDQS5jcnQwDAYDVR0TAQH/BAIwADCCAXwGCisGAQQB1nkCBAIEggFs\r\nBIIBaAFmAHUATnWjJ1yaEMM4W2zU3z9S6x3w4I4bjWnAsfpksWKaOd8AAAGOHuxW\r\nNwAABAMARjBEAiA794gDwBlLuPrnv5Fj4ablrQ0rdN79WXYKElFRlZfFwQIgbSkU\r\n2m9OuKVbhYkYye2p7uEZaY+7CIau2CgGn021hb4AdgB9WR4S4XgqexxhZ3xe/fjQ\r\nh1wUoE6VnrkDL9kOjC55uAAAAY4e7FX0AAAEAwBHMEUCIH/TXkK2Wg7UAa1E0G0A\r\nBP2PZubHPXyzhtWUQWo0S7SyAiEAuKaUmmoOH7eS+cZXu18EwdU0b0/Fr4vTIeAW\r\ndBwuOOQAdQDm0jFjQHeMwRBBBtdxuc7B0kD2loSG+7qHMh39HjeOUAAAAY4e7FYQ\r\nAAAEAwBGMEQCIFsrE/dHNM1QbIclR/50AiCNtoKjcGJFoblgaVnWW/6uAiBA5EE+\r\nvX1dxUdluf6cktPuo0IxYZSd6WCG4zqBMR292TANBgkqhkiG9w0BAQsFAAOCAQEA\r\nvKdi82U0vGaCCAYN598wEN6Ktu+BeZp3W3p1iVRBZgY9l0JPjwWN8Apwm4BUUTp3\r\n00gpIfROKvyR1655B0QDv/oL1Wuz/zQ87kUGVZNNeac07+X2e6YP5sqrwF4ttWai\r\najFRa8M2Y6vEk+7EmSexynxJBRa86Aa4xogqlTv/7kXf7LrDzMTlfle7o2L7eqwd\r\nCIc7vCYw9XQ5K80d4Siy6xz+RSu7+Un8QlfAYB7z1o32uPEUihk05ulMiXJYvA0W\r\nOagItBsuMSzgwQ0KDC9EmDYmXE9xWtUolehmBGRyQw+/E7iVu4x4js1HRiD0M+s9\r\nbRQ14PLxRLqDKu8oqZ8DQA==\r\n-----END CERTIFICATE-----",
}

# These can be used to track single-step order checkouts.
HOOK_PAYMENT_CAPTURE_PENDING_V2 = ConstRequestData(
    body=b'{"id":"WH-9Y180613C5171350R-3A568107UP261041K","event_version":"1.0","create_time":"2018-08-15T20:03:06.086Z","resource_type":"capture","resource_version":"2.0","event_type":"PAYMENT.CAPTURE.PENDING","summary":"Payment pending for $ 2.51 USD","resource":{"id":"02T21492PP3782704","amount":{"currency_code":"USD","value":"2.51"},"final_capture":true,"seller_protection":{"status":"NOT_ELIGIBLE"},"status":"PENDING","status_details":{"reason":"UNILATERAL"},"create_time":"2018-08-15T20:02:40Z","update_time":"2018-08-15T20:02:40Z","links":[{"href":"https://api.paypal.com/v2/payments/captures/02T21492PP3782704","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v2/payments/captures/02T21492PP3782704/refund","rel":"refund","method":"POST"},{"href":"https://api.paypal.com/v2/checkout/orders/8PR65097T8571330M","rel":"up","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-9Y180613C5171350R-3A568107UP261041K","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-9Y180613C5171350R-3A568107UP261041K/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1137",
        "accept": "*/*",
        "paypal-transmission-id": "4cce5920-5106-11ef-84e2-f38df3f70683",
        "paypal-transmission-time": "2024-08-02T19:34:57Z",
        "paypal-transmission-sig": "Kg+nPYIGXGAVA5sELwiLBTVZwzwssEAt/DI3/xDsjzwd1OMvddW2tFSpx4twvxEZS32fGVxZ4XRMWaMXYSBlFC09RpYNbA16r/WP8YV3KjaSzAc+btQyfUSRypr1mUsuWRL0DJnkLoC/KhCa4m3ZKFD4bFo5ZlWzdG2u5QgzL+YC/YmAhJGtcv6CIEN1rWB5OWuupVLhb+qYjhUH+99xsc5U2CihB65HFbtQqagX7YNFtOxEF5ckqSdgAYoMPECBCX8zOrDMy2UUaIvQpyhm0G3MF/IG3IPnRgP+ycN+AOjdsBGAWWwtZoXTPQ0mKH7oop4OrMNy4BPfE/8agUDxkw==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "1e7e973360d91",
        "x-b3-spanid": "c9e93947b749c4de",
    },
)
HOOK_PAYMENT_CAPTURE_COMPLETED_V2 = ConstRequestData(
    body=b'{"id":"WH-58D329510W468432D-8HN650336L201105X","event_version":"1.0","create_time":"2019-02-14T21:50:07.940Z","resource_type":"capture","resource_version":"2.0","event_type":"PAYMENT.CAPTURE.COMPLETED","summary":"Payment completed for $ 30.0 USD","resource":{"id":"12A34567BC123456S","amount":{"currency_code":"USD","value":"30.00"},"final_capture":true,"seller_protection":{"status":"ELIGIBLE","dispute_categories":["ITEM_NOT_RECEIVED","UNAUTHORIZED_TRANSACTION"]},"disbursement_mode":"INSTANT","seller_receivable_breakdown":{"gross_amount":{"currency_code":"USD","value":"30.00"},"paypal_fee":{"currency_code":"USD","value":"1.54"},"platform_fees":[{"amount":{"currency_code":"USD","value":"2.00"},"payee":{"merchant_id":"ABCDEFGHIJKL1"}}],"net_amount":{"currency_code":"USD","value":"26.46"}},"invoice_id":"5840243-146","status":"COMPLETED","supplementary_data":{"related_ids":{"order_id":"1AB234567A1234567"}},"create_time":"2022-08-23T18:29:50Z","update_time":"2022-08-23T18:29:50Z","links":[{"href":"https://api.paypal.com/v2/payments/captures/12A34567BC123456S","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v2/payments/captures/12A34567BC123456S/refund","rel":"refund","method":"POST"},{"href":"https://api.paypal.com/v2/checkout/orders/1AB234567A1234567","rel":"up","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-58D329510W468432D-8HN650336L201105X","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-58D329510W468432D-8HN650336L201105X/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1596",
        "accept": "*/*",
        "paypal-transmission-id": "1c6772d0-5106-11ef-9b66-89f3f924d48a",
        "paypal-transmission-time": "2024-08-02T19:33:35Z",
        "paypal-transmission-sig": "KY8qkrrIcGAyKS4VNgYlgP0iWIgeFEa3Y4q14d7mStEdJQbiEMhyB9/2cR85tjTlAmJ4NFxBW3BFdrFn7EukmdSw2RFkaCfSmzZoq8Uzjp1y6h9Uo307qte0hkuDHLLW07EvflOfS0Q2mNd+WPsmCilVYRAw9Acv6O8qVHAdVjINRoSeS5vISIDN7vaj0rBValwU8GE36rfFpUz1BvJqY2JaZc7wL0UYYB+xLneQWdOy4woa8MWUGVqFkJ9h/RLZsAIoMlOikAljETFIdGKiNr23GILoa1yM8/y+Oi1KM2DOJlEeywiR0BU5bhPjIsy8gsdwTyadbF1BCkFJcyGIlg==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "8622432c697e5",
        "x-b3-spanid": "6cc9dda341a8eada",
    },
)
HOOK_PAYMENT_CAPTURE_REFUNDED_V2 = ConstRequestData(
    body=b'{"id":"WH-1GE84257G0350133W-6RW800890C634293G","event_version":"1.0","create_time":"2018-08-15T19:14:04.543Z","resource_type":"refund","resource_version":"2.0","event_type":"PAYMENT.CAPTURE.REFUNDED","summary":"A $ 0.99 USD capture payment was refunded","resource":{"id":"1Y107995YT783435V","amount":{"currency_code":"USD","value":"0.99"},"seller_payable_breakdown":{"gross_amount":{"currency_code":"USD","value":"0.99"},"paypal_fee":{"currency_code":"USD","value":"0.02"},"net_amount":{"currency_code":"USD","value":"0.97"},"total_refunded_amount":{"currency_code":"USD","value":"1.98"}},"status":"COMPLETED","create_time":"2018-08-15T12:13:29-07:00","update_time":"2018-08-15T12:13:29-07:00","links":[{"href":"https://api.paypal.com/v2/payments/refunds/1Y107995YT783435V","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v2/payments/captures/0JF852973C016714D","rel":"up","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-1GE84257G0350133W-6RW800890C634293G","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-1GE84257G0350133W-6RW800890C634293G/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1192",
        "accept": "*/*",
        "paypal-transmission-id": "51730200-5106-11ef-9a30-157053fd3e43",
        "paypal-transmission-time": "2024-08-02T19:35:04Z",
        "paypal-transmission-sig": "ff31fhZxoix1VbYc2wPp991eiUBdhALb71NFSq8VOMkbaBdx3Gm4lFZmQDL/lUXl4rImLjUdDvBMp4DOCN7T5WmyY7G88yzMJJCngENSA7+r1NXweP+TLy5/jyGoNU2j3VEUSr9gwNF1tKrCpixnJbzwTA7tI8s4c53xfdtPuYKd4KNjH7jRQXt/YH+sR9hwNZTPWpIUm1LrdGFxCH1iHoM5/mO1E7EngRuTf8zYAFIJE/vBcY2dLoD2gTJPfLbo5D+KSSMqgrD+xuCPJtZnQjP9QbA0rUAenRYAbRxPh2u3dLTiAaRMP7mZBI4d9ecPkdk0HgtUAPVhJTTBmx+Lag==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "34da5ac816797",
        "x-b3-spanid": "2d01b91b31fa9b6c",
    },
)
HOOK_PAYMENT_CAPTURE_REVERSED_V2 = ConstRequestData(
    body=b'{"id":"WH-6F207351SC284371F-0KX52201050121307","event_version":"1.0","create_time":"2018-08-15T21:30:35.780Z","resource_type":"refund","resource_version":"2.0","event_type":"PAYMENT.CAPTURE.REVERSED","summary":"A $ 2.51 USD capture payment was reversed","resource":{"id":"09E71677NS257044M","amount":{"currency_code":"USD","value":"2.51"},"note_to_payer":"Payment reversed","seller_payable_breakdown":{"gross_amount":{"currency_code":"USD","value":"2.51"},"paypal_fee":{"currency_code":"USD","value":"0.00"},"net_amount":{"currency_code":"USD","value":"2.51"},"total_refunded_amount":{"currency_code":"USD","value":"2.51"}},"status":"COMPLETED","create_time":"2018-08-15T14:30:10-07:00","update_time":"2018-08-15T14:30:10-07:00","links":[{"href":"https://api.paypal.com/v2/payments/refunds/09E71677NS257044M","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v2/payments/captures/4L335234718889942","rel":"up","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-6F207351SC284371F-0KX52201050121307","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-6F207351SC284371F-0KX52201050121307/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1227",
        "accept": "*/*",
        "paypal-transmission-id": "55266d10-5106-11ef-9a30-157053fd3e43",
        "paypal-transmission-time": "2024-08-02T19:35:11Z",
        "paypal-transmission-sig": "aViMsu1a/dLFH1RdcaSCsRchGLui3tLMvFwEx8W9D0FgG0hYt+yKUHjTjtLrHKXChwx5K0+Ad0gtMywRgW0DhEKcEwry34T9rrPDxsdYKT88g2MwnhEsAl7bDFwfiwbM9lg7YMJcGukXisZTNga5IJx/ywbmhgVXmdgUhjJQevDsStBL79ZpzLsdlMmfufIyddrDmpUvIXFH10vspzSiaIlQH2xg7K1FI5FDa+Y0eAjmD245YHIhob7kZUOK70EVZPtF9n6fYQ5wZwfg/H6nd1NVSGlBjiTqvSY9hV8d2xbTmFaSPKObHUwxAA+4lGtcrKnlXqG57+B2R+SS8vnYGA==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "acdd2a0536b10",
        "x-b3-spanid": "5ae6310c43c5d7d7",
    },
)
HOOK_PAYMENT_CAPTURE_DECLINED_V2 = ConstRequestData(
    body=b'{"id":"WH-6HE329230C693231F-5WV60586YA659351G","event_version":"1.0","create_time":"2022-12-13T19:13:07.251Z","resource_type":"capture","resource_version":"2.0","event_type":"PAYMENT.CAPTURE.DECLINED","summary":"A payment capture for $ 185.1 USD was declined.","resource":{"id":"7U133281TB3277326","amount":{"currency_code":"USD","value":"185.10"},"final_capture":false,"seller_protection":{"status":"ELIGIBLE","dispute_categories":["ITEM_NOT_RECEIVED","UNAUTHORIZED_TRANSACTION"]},"disbursement_mode":"INSTANT","seller_receivable_breakdown":{"gross_amount":{"currency_code":"USD","value":"185.10"},"platform_fees":[{"amount":{"currency_code":"USD","value":"0.50"},"payee":{"merchant_id":"QG3ECYYLJ2A48"}}],"net_amount":{"currency_code":"USD","value":"184.60"},"receivable_amount":{"currency_code":"EUR","value":"115.98"},"exchange_rate":{"source_currency":"USD","target_currency":"EUR","value":"0.628281035098039"}},"invoice_id":"ARG0-2022-12-08T21:00:21.564Z-435","custom_id":"CUSTOMID-1001","status":"DECLINED","supplementary_data":{"related_ids":{"order_id":"48R416400V564864N","authorization_id":"24B76447NN600461P"}},"create_time":"2022-12-13T19:13:00Z","update_time":"2022-12-13T19:13:00Z","links":[{"href":"https://api.paypal.com/v2/payments/captures/7U133281TB3277326","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v2/payments/captures/7U133281TB3277326/refund","rel":"refund","method":"POST"},{"href":"https://api.paypal.com/v2/payments/authorizations/24B76447NN600461P","rel":"up","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-6HE329230C693231F-5WV60586YA659351G","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-6HE329230C693231F-5WV60586YA659351G/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1813",
        "accept": "*/*",
        "paypal-transmission-id": "3ed00ad0-5106-11ef-811d-8beb274ff66b",
        "paypal-transmission-time": "2024-08-02T19:34:33Z",
        "paypal-transmission-sig": "O3XQypYDh/gSvvIE2Mj7H+hbcoD3T7OZwWYgiZ10DQxpyF3KK2DiiVJiNwagSC/ah5yYb8XkYMkFLLQxm/wzH7zJPP9HV7nfDyc5gDO2gINgu3hAnxyNDHJBvNWIyLTTsK3KDc7zi3E1KRv74XSbsfAYIaULntjGn2EMEjG+TCfHof7a/AUMX5I5KdLVK7QCt5OorvxGm0ermOXR778bN+/jyQ2R7EuNJuB0GDwsja3UHMI80v7OexDaHeRb4NAecvLP6xaFoKWErFUyGkcwkFoAwaGuM7sGByJuBPfqXgtLsBR8+4bWsNZJsQjZEwxMhLw3puw/M01vpGfpUvknAg==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "7647eb4b4c677",
        "x-b3-spanid": "31c39634469dd9a1",
    },
)
# NOTE: HOOK_PAYMENT_CAPTURE_DENIED_V2 is not relevant to the v2 payments/orders API seemingly.

# These can be used to track subscription state for an account.
HOOK_SUBSCRIPTION_CREATED_v2 = ConstRequestData(
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
HOOK_SUBSCRIPTION_EXPIRED_V2 = ConstRequestData(  # NOTE: seems to not have V1
    body=b'{"id":"WH-UY687577TY25889J9-2R6T55435R66168Y6","create_time":"2018-19-12T22:20:32.000Z","event_type":"BILLING.SUBSCRIPTION.EXPIRED","event_version":"1.0","resource_type":"subscription","resource_version":"2.0","summary":"A billing agreement has expired.","resource":{"id":"I-BW452GLLEP1G","status":"EXPIRED","status_update_time":"2018-12-10T21:20:49Z","plan_id":"P-5ML4271244454362WXNWU5NQ","start_time":"2018-11-01T00:00:00Z","quantity":"20","shipping_amount":{"currency_code":"USD","value":"10.00"},"subscriber":{"name":{"given_name":"John","surname":"Doe"},"email_address":"customer@example.com","shipping_address":{"name":{"full_name":"John Doe"},"address":{"address_line_1":"2211 N First Street","address_line_2":"Building 17","admin_area_2":"San Jose","admin_area_1":"CA","postal_code":"95131","country_code":"US"}}},"auto_renewal":true,"billing_info":{"outstanding_balance":{"currency_code":"USD","value":"10.00"},"cycle_executions":[{"tenure_type":"TRIAL","sequence":1,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1},{"tenure_type":"REGULAR","sequence":2,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1}],"last_payment":{"amount":{"currency_code":"USD","value":"500.00"},"time":"2018-12-01T01:20:49Z"},"next_billing_time":"2019-01-01T00:20:49Z","final_payment_time":"2020-01-01T00:20:49Z","failed_payments_count":2},"create_time":"2018-12-10T21:20:49Z","update_time":"2018-12-10T21:20:49Z","links":[{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G","rel":"self","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-UY687577TY25889J9-2R6T55435R66168Y6","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-UY687577TY25889J9-2R6T55435R66168Y6/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1858",
        "accept": "*/*",
        "paypal-transmission-id": "a33480d0-4e97-11ef-9e27-51575aa603e3",
        "paypal-transmission-time": "2024-07-30T17:17:45Z",
        "paypal-transmission-sig": "oV/imHm524TdYHzXvvOPJog8LSOW8nmN0vFxrXp4U6A9SG43JJlkD4dz3Vh9chP3vBe3gG+daeMKXcJZRwxf3Kiag+iasCPsf54ngSHJYVP8DBJg1XQPtyaH/81owuUJqpvHXe2lBvPfcWFoaLOsvfNEkeOWhPdWkQQflJZx6OExZU9axec+6AcU2UjHKRvuas37IxBqGjk8FtPdplQ4snqxo0ZPCqBoMjZIm6ssY5cwVXi2Cd90431fMDCG+G+vUvylc64btpA4soRLoEnGnNhRBYuJ0vcn4WipSvMPfTYNKSupWX3gYR0/S2x5Emk6vxwLkDOEAZsyZtURCVIwXw==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "d42d5930438e4",
        "x-b3-spanid": "835ee927519ede97",
    },
)
HOOK_SUBSCRIPTION_CANCELLED_V2 = ConstRequestData(
    body=b'{"id":"WH-UY687577TY25889J9-2R6T55435R66168Y6","create_time":"2018-19-12T22:20:32.000Z","event_type":"BILLING.SUBSCRIPTION.CANCELLED","event_version":"1.0","resource_type":"subscription","resource_version":"2.0","summary":"A billing subscription was cancelled.","resource":{"id":"I-BW452GLLEP1G","status":"CANCELLED","status_update_time":"2018-12-10T21:20:49Z","plan_id":"P-5ML4271244454362WXNWU5NQ","start_time":"2018-11-01T00:00:00Z","quantity":"20","shipping_amount":{"currency_code":"USD","value":"10.00"},"subscriber":{"name":{"given_name":"John","surname":"Doe"},"email_address":"customer@example.com","shipping_address":{"name":{"full_name":"John Doe"},"address":{"address_line_1":"2211 N First Street","address_line_2":"Building 17","admin_area_2":"San Jose","admin_area_1":"CA","postal_code":"95131","country_code":"US"}}},"auto_renewal":true,"billing_info":{"outstanding_balance":{"currency_code":"USD","value":"10.00"},"cycle_executions":[{"tenure_type":"TRIAL","sequence":1,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1},{"tenure_type":"REGULAR","sequence":2,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1}],"last_payment":{"amount":{"currency_code":"USD","value":"500.00"},"time":"2018-12-01T01:20:49Z"},"next_billing_time":"2019-01-01T00:20:49Z","final_payment_time":"2020-01-01T00:20:49Z","failed_payments_count":2},"create_time":"2018-12-10T21:20:49Z","update_time":"2018-12-10T21:20:49Z","links":[{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G","rel":"edit","method":"PATCH"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-UY687577TY25889J9-2R6T55435R66168Y6","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-UY687577TY25889J9-2R6T55435R66168Y6/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1971",
        "accept": "*/*",
        "paypal-transmission-id": "9af32930-4e97-11ef-94b8-bbc7b17d2f32",
        "paypal-transmission-time": "2024-07-30T17:17:31Z",
        "paypal-transmission-sig": "Htj4GiEIZmWgoRW53ACxVjt9K5SJw8RNsXaqP+tlgJrvm+ljRm9T3zwCrRvZKDsK0EGmZaLBvFUgsxVAdCt5REt/32aTL++XaK7zewq1wIrZlND4GVkqnfy0AvX3bRQyqSTvb2k/EQ76vvPrbSfDKssMWNGwPz79ZvagR7ikkZhzIlgEafXIQEsx48j6OUQgYjy1Ll76Oy4pZeC0NDpOK20NvrvK8CAquE5/id3NkN6WPrfMiGfUdZhnJ8evkMJOXX/RehhQZynxtNGqV1CLyMJxa7EUkrc12+N1aOWbGTH+aMZYYpblZOpjLjHnIcD91JmO/3P/jUHoP5AEQII7HQ==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "706b42b959b3b",
        "x-b3-spanid": "cac887583bd013cc",
    },
)
HOOK_SUBSCRIPTION_PAYMENT_FAILED_V2 = ConstRequestData(  # NOTE: seems to not have V1
    body=b'{"id":"WH-77687562XN25889J2-8Y6T55435R66168T4","create_time":"2019-01-01T01:20:54.000Z","event_type":"BILLING.SUBSCRIPTION.PAYMENT.FAILED","event_version":"1.0","resource_type":"subscription","resource_version":"2.0","summary":"Subscription payment failed","resource":{"id":"I-BW452GLLEP1G","status":"ACTIVE","status_update_time":"2018-12-10T21:20:49Z","plan_id":"P-5ML4271244454362WXNWU5NQ","start_time":"2018-11-01T00:00:00Z","quantity":"20","shipping_amount":{"currency_code":"USD","value":"10.00"},"subscriber":{"name":{"given_name":"John","surname":"Doe"},"email_address":"customer@example.com","payer_id":"2J6QB8YJQSJRJ","shipping_address":{"name":{"full_name":"John Doe"},"address":{"address_line_1":"2211 N First Street","address_line_2":"Building 17","admin_area_2":"San Jose","admin_area_1":"CA","postal_code":"95131","country_code":"US"}}},"billing_info":{"outstanding_balance":{"currency_code":"USD","value":"10.00"},"cycle_executions":[{"tenure_type":"TRIAL","sequence":1,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1},{"tenure_type":"REGULAR","sequence":2,"cycles_completed":1,"cycles_remaining":0,"current_pricing_scheme_version":1}],"last_payment":{"amount":{"currency_code":"USD","value":"500.00"},"time":"2018-12-01T01:20:49Z"},"last_failed_payment":{"amount":{"currency_code":"USD","value":"500.00"},"time":"2019-01-01T01:20:49Z","reason_code":"PAYMENT_DENIED","next_payment_retry_date":"2019-01-06T01:20:49Z"},"next_billing_time":"2019-01-01T00:20:49Z","final_payment_time":"2020-01-01T00:20:49Z","failed_payments_count":2},"create_time":"2018-10-20T21:20:49Z","update_time":"2018-12-10T21:20:49Z","links":[{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G?fields=last_failed_payment","rel":"self","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-77687562XN25889J2-8Y6T55435R66168T4","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-77687562XN25889J2-8Y6T55435R66168T4/resend","rel":"resend","method":"POST"},{"href":"https://api.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G","rel":"subscription","method":"GET"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "2187",
        "accept": "*/*",
        "paypal-transmission-id": "a6a871e0-4e97-11ef-ba7c-5f4ee39b3f69",
        "paypal-transmission-time": "2024-07-30T17:17:51Z",
        "paypal-transmission-sig": "jtxM/RdL/T9H5xtt9NBKBY52ss52ysuudI7saN+rUNtfuyJHi1OhxY7tWn2s0k3oqFtgzLozvqunKSoi0L2FrFdnu8/W2nsZbxpIwEYPhQvz5eP22nrlS2GH0X+PLDaS+mP59lNeqgW9Hk2QgFx1lrKu9kcm15XIlhxWVPSbtbEYp7G/Ds379g4GSr4IuXdE2CFhqm2rSEn2JcMIk74VExKKqLh2caammyjSyN/gpcAys2EgsgHJW9nZd/lHD4VSPzVbtLJsUobQ6HWz5vx4eeGlMUEopwk9Kj7oLCbHZDNK7Tg3EKuvjsEIhjxUXmwaSxRbNyw2igV8xpmKx2gnUw==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "954a951c61fa6",
        "x-b3-spanid": "78fcc92dddf9e465",
    },
)
# NOTE: there is also suspend and activate events for subscription.

# These can be used to track subscription payment crediting.
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
HOOK_PAYMENT_SALE_REVERSED = ConstRequestData(
    body=b'{"id":"WH-3EC545679X386831C-3D038940937933201","event_version":"1.0","create_time":"2014-10-23T00:19:27Z","resource_type":"sale","event_type":"PAYMENT.SALE.REVERSED","summary":"A $ 0.49 USD sale payment was reversed","resource":{"id":"77689802DL785834G","create_time":"2014-10-23T00:19:12Z","state":"completed","amount":{"total":"-0.49","currency":"USD","details":{"subtotal":"-0.64","tax":"0.08","shipping":"0.07"}},"links":[{"href":"https://api.paypal.com/v1/payments/refund/77689802DL785834G","rel":"self","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-3EC545679X386831C-3D038940937933201","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-3EC545679X386831C-3D038940937933201/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "815",
        "accept": "*/*",
        "paypal-transmission-id": "46b39690-4e8b-11ef-9e80-11cd83efcb94",
        "paypal-transmission-time": "2024-07-30T15:49:16Z",
        "paypal-transmission-sig": "A4TGppWtAke3fbrFNNcqeXW317IROcwc6yyRSjrRkK+WqRaFrTXL9ny+qwZTw9Zt17SSlek7Aon15MtvS4C8eRdokCRuljAqXHRaK2jO5A48VQXcyldy2hI90oYB/ETqCsmQjQJX7Bkd5co1fPKnCyR34HAdNjPMvnZMyL7/RmEUIAwayJ1ge4e9ghTmz9n1lQ1/HJGEPprPs4FmwDDBKQS4Ttf22Qv14Hh4XpzWWpaWF1OYPN9/LRueR0Dh+0WExU94YvbwL6Wgh1/lAelCdq5W8T1D/iXB0IQudUAZuc9EmzF5Qwjt8+YsVkYZC1+UgdoIFN2BRk3k55ogomnaOA==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "c904ae4610304",
        "x-b3-spanid": "734e6ac4084cd6bd",
    },
)
HOOK_PAYMENT_SALE_REFUNDED = ConstRequestData(
    body=b'{"id":"WH-2N242548W9943490U-1JU23391CS4765624","event_version":"1.0","create_time":"2014-10-31T15:42:24Z","resource_type":"sale","event_type":"PAYMENT.SALE.REFUNDED","summary":"A 0.01 USD sale payment was refunded","resource":{"id":"6YX43824R4443062K","create_time":"2014-10-31T15:41:51Z","update_time":"2014-10-31T15:41:51Z","state":"completed","amount":{"total":"-0.01","currency":"USD"},"sale_id":"9T0916710M1105906","parent_payment":"PAY-5437236047802405NKRJ22UA","links":[{"href":"https://api.paypal.com/v1/payments/refund/6YX43824R4443062K","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/payments/payment/PAY-5437236047802405NKRJ22UA","rel":"parent_payment","method":"GET"},{"href":"https://api.paypal.com/v1/payments/sale/9T0916710M1105906","rel":"sale","method":"GET"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-2N242548W9943490U-1JU23391CS4765624","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-2N242548W9943490U-1JU23391CS4765624/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1084",
        "accept": "*/*",
        "paypal-transmission-id": "5e7ee590-4e8b-11ef-bc13-fd5b69793a44",
        "paypal-transmission-time": "2024-07-30T15:49:56Z",
        "paypal-transmission-sig": "UEbqoqrTs2SgWwaNF1IJbbDDfJmwWKw3Cj0DC40eI5RQOWbRlEivkOzjke8U50MUckFDvGLIBRKWJxfE8jGYNv2roaRgM4EMwlyT+2lOOVFbkFc6O7xwr5QcYWGOPK2PQ4ZuGl3VOmjNdOUcLxt2A0l8tktXWeMP3rY5Fh4+UqhfqoX0RTjKUkBZDHZxt+jzr43v0+Oe6c8Yp8s2aGaSgUCNXO5b5tcDlxhI2DNzysndnQfolzHuyAVo4K7u9PNbwJg835T2ne7bzUNB6QvgzP3Y7CcyR9w3sqjpn87dF9wEATDr2tj34ASIAOere1RSowrp91k8b6chcOSKtVCcUg==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "1f907429ca855",
        "x-b3-spanid": "15fd291e4d83a267",
    },
)

# Useful for tracking details of a subscription plan for the server. (they are primarily managed on the PayPal account)
HOOK_PLAN_CREATED_V2 = ConstRequestData(
    body=b'{"id":"WH-9BC87562XN2588303-1GN955435R661687G","create_time":"2018-19-12T22:20:32.000Z","event_type":"BILLING.PLAN.CREATED","event_version":"1.0","resource_type":"plan","resource_version":"2.0","summary":"A billing plan was created.","resource":{"id":"P-7GL4271244454362WXNWU5NQ","product_id":"PROD-XXCD1234QWER65782","name":"Zoho Marketing Campaign  Plan","description":"Zoho Marketing Campaign Plan","status":"ACTIVE","usage_type":"LICENSED","billing_cycles":[{"frequency":{"interval_unit":"MONTH","interval_count":1},"tenure_type":"TRIAL","sequence":1,"total_cycles":1,"pricing_scheme":{"fixed_price":{"value":"50","currency_code":"USD"},"tier_mode":"VOLUME","tiers":[{"starting_quantity":"1","ending_quantity":"1000","amount":{"value":"100","currency_code":"USD"}},{"starting_quantity":"1001","amount":{"value":"200","currency_code":"USD"}}]}},{"frequency":{"interval_unit":"MONTH","interval_count":1},"tenure_type":"REGULAR","sequence":2,"total_cycles":12,"pricing_scheme":{"fixed_price":{"value":"100","currency_code":"USD"},"tier_mode":"VOLUME","tiers":[{"starting_quantity":"1","ending_quantity":"1000","amount":{"value":"300","currency_code":"USD"}},{"starting_quantity":"1001","amount":{"value":"1000","currency_code":"USD"}}]}}],"payment_preferences":{"service_type":"PREPAID","auto_bill_outstanding":true,"setup_fee":{"value":"10","currency_code":"USD"},"setup_fee_failure_action":"CONTINUE","payment_failure_threshold":3},"taxes":{"percentage":"10","inclusive":false},"create_time":"2018-12-10T21:20:49Z","update_time":"2018-12-10T21:20:49Z","links":[{"href":"https://api.paypal.com/v1/billing/plans/P-5ML4271244454362WXNWU5NQ","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/billing/plans/P-5ML4271244454362WXNWU5NQ","rel":"edit","method":"PATCH"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-9BC87562XN2588303-1GN955435R661687G","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-9BC87562XN2588303-1GN955435R661687G/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "2068",
        "accept": "*/*",
        "paypal-transmission-id": "61520c50-4e97-11ef-b13a-bba97e37ef15",
        "paypal-transmission-time": "2024-07-30T17:15:55Z",
        "paypal-transmission-sig": "KV4k6MMiM8B3oHBBdih+u6uaauQCD4PFkHYQomo/hGPmetOmIcxtXLG6OpsJFhoW6aQ4hMiUoMKsbHGhHKT6XvdRzMLu/ZeKHDo5bIUGHVOjL3ZgLdLuN1k4J+dNvyFfVtoExASwRVqFf140Sg0REjd4qcBiMnnw8GBGWG2GUgTj9OiJlQ1NC6ZbWH8JwzYvqzEwsZLoqZtw/5MNpD5VJtdAVVLlaMDl4878FT7Rk8oQuePsftifd+3JYVfn3ou6X5x3/o+t9zh8lYCx1L4ksHiXPT1NVhYgXmdabJebb9jdiyP/wQb5c44wVXpFTAF/6u+xrfzEr51E3wfN5KGjtg==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "69e23aff16371",
        "x-b3-spanid": "f55aae7597d94f9d",
    },
)
HOOK_PLAN_UPDATED_V2 = ConstRequestData(
    body=b'{"id":"WH-55TG7562XN2588878-8YH955435R661687G","create_time":"2018-19-12T22:20:32.000Z","event_type":"BILLING.PLAN.UPDATED","event_version":"1.0","resource_type":"plan","resource_version":"2.0","summary":"A billing plan was updated.","resource":{"id":"P-7GL4271244454362WXNWU5NQ","product_id":"PROD-XXCD1234QWER65782","name":"Zoho Marketing Campaign  Plan","description":"Zoho Marketing Campaign Plan","status":"ACTIVE","usage_type":"LICENSED","billing_cycles":[{"frequency":{"interval_unit":"MONTH","interval_count":1},"tenure_type":"TRIAL","sequence":1,"total_cycles":1,"pricing_scheme":{"fixed_price":{"value":"50","currency_code":"USD"},"tier_mode":"VOLUME","tiers":[{"starting_quantity":"1","ending_quantity":"1000","amount":{"value":"100","currency_code":"USD"}},{"starting_quantity":"1001","amount":{"value":"200","currency_code":"USD"}}]}},{"frequency":{"interval_unit":"MONTH","interval_count":1},"tenure_type":"REGULAR","sequence":2,"total_cycles":12,"pricing_scheme":{"fixed_price":{"value":"100","currency_code":"USD"},"tier_mode":"VOLUME","tiers":[{"starting_quantity":"1","ending_quantity":"1000","amount":{"value":"300","currency_code":"USD"}},{"starting_quantity":"1001","amount":{"value":"1000","currency_code":"USD"}}]}}],"payment_preferences":{"service_type":"PREPAID","auto_bill_outstanding":true,"setup_fee":{"value":"10","currency_code":"USD"},"setup_fee_failure_action":"CONTINUE","payment_failure_threshold":3},"taxes":{"percentage":"10","inclusive":false},"create_time":"2018-12-10T21:20:49Z","update_time":"2018-12-10T21:20:49Z","links":[{"href":"https://api.paypal.com/v1/billing/plans/P-5ML4271244454362WXNWU5NQ","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/billing/plans/P-5ML4271244454362WXNWU5NQ","rel":"edit","method":"PATCH"}]},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-55TG7562XN2588878-8YH955435R661687G","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-55TG7562XN2588878-8YH955435R661687G/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "2068",
        "accept": "*/*",
        "paypal-transmission-id": "74ab0d10-4e97-11ef-9e8c-3b5622a57e72",
        "paypal-transmission-time": "2024-07-30T17:16:27Z",
        "paypal-transmission-sig": "k5BXXlBepSvWkmHthtaQu69vzq0gNdXbcIrsHZueoC/NiEg6NxPsm0YsbI5vcxhCGOAgZA3JpER1WwTxzgY8Cd3ndFXDqMdNwYsgX9gxYuprtJC1T/U0RZsZyqcOlDSCjtSbr3akq+pbTyar3/GLbWazOWikJM7AbtEpzjactUwBIT7Jtqk/Njeum2E//DU9bjV4EqndNzoSAmWPnau+Bkru8pFTaGCMmZZ97iWOsiQdiri8YvsecSTTwtukGv1/bY1NKNO2v07s9NMWQjAQ00O57N2K1sK3ZhJnP9B6PNdZ8QPjXQJ4cs6fvrM1zPrauyt9WmyafRZi4CWHYs1NBg==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "a6ec509ee22c2",
        "x-b3-spanid": "c75175a3593afcac",
    },
)

# Deprecated, only for reference.
HOOK_SUBSCRIPTION_CREATED_v1 = ConstRequestData(
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
HOOK_SUBSCRIPTION_CANCELLED_V1 = ConstRequestData(
    body=b'{"id":"WH-6TD369808N914414D-1YJ376786E892292F","event_version":"1.0","create_time":"2016-04-28T11:53:10Z","resource_type":"Agreement","event_type":"BILLING.SUBSCRIPTION.CANCELLED","summary":"A billing subscription was cancelled","resource":{"id":"I-PE7JWXKGVN0R","shipping_address":{"recipient_name":"Cool Buyer","line1":"3rd st","line2":"cool","city":"San Jose","state":"CA","postal_code":"95112","country_code":"US"},"plan":{"curr_code":"USD","links":[],"payment_definitions":[{"type":"TRIAL","frequency":"Month","frequency_interval":"1","amount":{"value":"5.00"},"cycles":"5","charge_models":[{"type":"TAX","amount":{"value":"1.00"}},{"type":"SHIPPING","amount":{"value":"1.00"}}]},{"type":"REGULAR","frequency":"Month","frequency_interval":"1","amount":{"value":"10.00"},"cycles":"15","charge_models":[{"type":"TAX","amount":{"value":"2.00"}},{"type":"SHIPPING","amount":{"value":"1.00"}}]}],"merchant_preferences":{"setup_fee":{"value":"0.00"},"auto_bill_amount":"YES","max_fail_attempts":"21"}},"payer":{"payment_method":"paypal","status":"verified","payer_info":{"email":"coolbuyer@example.com","first_name":"Cool","last_name":"Buyer","payer_id":"XLHKRXRA4H7QY","shipping_address":{"recipient_name":"Cool Buyer","line1":"3rd st","line2":"cool","city":"San Jose","state":"CA","postal_code":"95112","country_code":"US"}}},"agreement_details":{"outstanding_balance":{"value":"0.00"},"num_cycles_remaining":"5","num_cycles_completed":"0","last_payment_date":"2016-04-28T11:29:54Z","last_payment_amount":{"value":"1.00"},"final_payment_due_date":"2017-11-30T10:00:00Z","failed_payment_count":"0"},"description":"update desc","state":"Cancelled","links":[{"href":"https://api.paypal.com/v1/payments/billing-agreements/I-PE7JWXKGVN0R","rel":"self","method":"GET"}],"start_date":"2016-04-30T07:00:00Z"},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-6TD369808N914414D-1YJ376786E892292F","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-6TD369808N914414D-1YJ376786E892292F/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.140",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "2090",
        "accept": "*/*",
        "paypal-transmission-id": "935ae2d0-4e97-11ef-883d-091977c746ee",
        "paypal-transmission-time": "2024-07-30T17:17:19Z",
        "paypal-transmission-sig": "NCb0Ps6YfAnA6bsQ25MuasF47q7DOeQcbB4P1HnIT8tEKIc8LwvNiNffdDVWNxsZmlqILiDLtyFsUJijV7C46FGRysXOWmLVYOdp+4vapbIzuD+VDO38giHDWsWgbo8cXuY8TVlJ7W9WyM48Buka96BmwqixIj8qCcIcUpTYD9aDHE5IKJ9G1vbdN8LeTCrhwG+CHmndYimCsTIcyhLvRe4SKB9djsPbBXd03+ve/bxzBrmQehaGqykUJWm7ejYxwnDvFPnwCxNW1cx760AWpGoqAfh6YWKIR5AqK+riVcgKtuQQRPMl2TDrjHz2tiYWB9SYvXPzsxiLp8re9dPZ6w==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "7335e98c39f2c",
        "x-b3-spanid": "b099cfce3828f8d",
    },
)
HOOK_PLAN_CREATED_V1 = ConstRequestData(
    body=b'{"id":"WH-2N1678257S892762B-8MC99539P4557624Y","event_version":"1.0","create_time":"2016-04-28T11:21:44Z","resource_type":"plan","event_type":"BILLING.PLAN.CREATED","summary":"A billing plan was created","resource":{"id":"P-7LT50814996943336LSNDODY","merchant_preferences":{"setup_fee":{"currency":"USD","value":"1"},"return_url":"http://www.paypal.com","cancel_url":"http://www.yahoo.com","auto_bill_amount":"YES","initial_fail_amount_action":"CONTINUE","max_fail_attempts":"21"},"update_time":"2016-04-28T11:21:31.151Z","description":"test web new","payment_definitions":[{"name":"Payment Definition-1","type":"REGULAR","frequency":"Month","frequency_interval":"1","amount":{"currency":"USD","value":"10"},"cycles":"15","charge_models":[{"type":"SHIPPING","amount":{"currency":"USD","value":"1"},"id":"CHM-29V063578B632154XLSNDODY"},{"type":"TAX","amount":{"currency":"USD","value":"2"},"id":"CHM-72N78855RJ303084YLSNDODY"}],"id":"PD-28U66480VB469201XLSNDODY"},{"name":"Payment Definition-2","type":"TRIAL","frequency":"Month","frequency_interval":"1","amount":{"currency":"USD","value":"5"},"cycles":"5","charge_models":[{"type":"SHIPPING","amount":{"currency":"USD","value":"1"},"id":"CHM-4CT119433N5199501LSNDODY"},{"type":"TAX","amount":{"currency":"USD","value":"1"},"id":"CHM-38H015979N656741TLSNDODY"}],"id":"PD-99B78670BE878604GLSNDODY"}],"name":"Fast Speed Plan","state":"CREATED","create_time":"2016-04-28T11:21:31.151Z","links":[{"href":"https://api.paypal.com/v1/payments/billing-plans/P-7LT50814996943336LSNDODY","rel":"self","method":"GET"}],"type":"FIXED"},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-2N1678257S892762B-8MC99539P4557624Y","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-2N1678257S892762B-8MC99539P4557624Y/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1862",
        "accept": "*/*",
        "paypal-transmission-id": "51546b90-4e97-11ef-9e8c-3b5622a57e72",
        "paypal-transmission-time": "2024-07-30T17:15:28Z",
        "paypal-transmission-sig": "IH5jNrvcvrIBvVp4/SLyITu2zD1JkmlMcB8VjX+E9RL9OtA9G5Pkyvr/h15f2/Qm3RAiNWUly+KRiawU4VWxfrGI0MIWvGn/ccKcwssyMPnOCezPrjnB1z340UEktOejU0L19ZRDwY07Olp+vvMw46C4qO4Iy+klqFJZGMLcMLKBytfGCAYwxokRxG6VrVcXqr5nXZHZX7hX/4o+6noJ136jDaAHFbDYTVqPfMm05cB/QvYUjXZjn7wBPhaUDQCj+iF2LRoifQ5t7beEXJ76ye+J/arFCtpiBU7txcxMS14Ch4j9lRbhXHaney5X5s4jSXjBVtB5ZzINMC83YM6ueQ==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "05a8255b19153",
        "x-b3-spanid": "342da2c2cea763b7",
    },
)
HOOK_PLAN_UPDATED_V1 = ConstRequestData(
    body=b'{"id":"WH-303507964T970970H-60Y688551M4794625","event_version":"1.0","create_time":"2016-04-28T11:23:52Z","resource_type":"plan","event_type":"BILLING.PLAN.UPDATED","summary":"A billing plan was updated","resource":{"id":"P-7LT50814996943336LSNDODY","merchant_preferences":{"setup_fee":{"currency":"USD","value":"1"},"return_url":"http://www.paypal.com","cancel_url":"http://www.yahoo.com","auto_bill_amount":"YES","initial_fail_amount_action":"CONTINUE","max_fail_attempts":"21"},"update_time":"2016-04-28T11:23:27.568Z","description":"test web new","payment_definitions":[{"name":"Payment Definition-1","type":"REGULAR","frequency":"Month","frequency_interval":"1","amount":{"currency":"USD","value":"10"},"cycles":"15","charge_models":[{"type":"TAX","amount":{"currency":"USD","value":"2"},"id":"CHM-72N78855RJ303084YLSNDODY"},{"type":"SHIPPING","amount":{"currency":"USD","value":"1"},"id":"CHM-29V063578B632154XLSNDODY"}],"id":"PD-28U66480VB469201XLSNDODY"},{"name":"Payment Definition-2","type":"TRIAL","frequency":"Month","frequency_interval":"1","amount":{"currency":"USD","value":"5"},"cycles":"5","charge_models":[{"type":"TAX","amount":{"currency":"USD","value":"1"},"id":"CHM-38H015979N656741TLSNDODY"},{"type":"SHIPPING","amount":{"currency":"USD","value":"1"},"id":"CHM-4CT119433N5199501LSNDODY"}],"id":"PD-99B78670BE878604GLSNDODY"}],"name":"Fast Speed Plan","state":"ACTIVE","create_time":"2016-04-28T11:21:31.151Z","links":[{"href":"https://api.paypal.com/v1/payments/billing-plans/P-7LT50814996943336LSNDODY","rel":"self","method":"GET"}],"type":"FIXED"},"links":[{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-303507964T970970H-60Y688551M4794625","rel":"self","method":"GET"},{"href":"https://api.paypal.com/v1/notifications/webhooks-events/WH-303507964T970970H-60Y688551M4794625/resend","rel":"resend","method":"POST"}]}',
    headers={
        "x-real-ip": "173.0.81.65",
        "host": "127.0.0.1:8001",
        "connection": "close",
        "content-length": "1861",
        "accept": "*/*",
        "paypal-transmission-id": "6f279cf0-4e97-11ef-b534-cd5b30b8aa03",
        "paypal-transmission-time": "2024-07-30T17:16:18Z",
        "paypal-transmission-sig": "Mrq8zF/xAL6zLvViyjIV4oqURWp4flIpm9cW25ivqvXm0zFSvtAIUVi7nGHDOMJ+Cq3VIgJsYQ0BJMLFHA0Vv7/JCR81tsMcyyjGuvge0YSKIW96n321i09FIEnZVhUgWy8sD1YuP7s3JxngcwTDkCr7eBRCQAXNURXWE8yJIa/edAA3X90fju6niiVSefw3NpJmodrZ66IUyfNWmjfUyDeIOlMkAwqkCmWdSkj4/B5u19Sen8geH6wONyBE9lYkcYZZkyEtXcqKdvGPNPyCkbaCzZqstnkVOZUhDzOhFg+CS35EnqlmuZ8dknLfSBfGju7V5HmamveOXFuJ+TVZZQ==",
        "paypal-auth-version": "v2",
        "paypal-cert-url": "https://api.paypal.com/v1/notifications/certs/CERT-360caa42-fca2a594-1a5f47cb",
        "paypal-auth-algo": "SHA256withRSA",
        "content-type": "application/json",
        "user-agent": "PayPal/AUHD-214.0-58391792",
        "correlation-id": "5f8ca3951d372",
        "x-b3-spanid": "6aea22100ef6e269",
    },
)

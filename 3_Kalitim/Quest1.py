""" +> WebPush isimli bir class tanımlayınız. +>Platform, optin, global_frequency_capping, start_date, end_date,
language, push_type isimli özniteliklere sahip olsun. X> optin değeri boolean değer alsın. +>TriggerPush, BulkPush,
SegmentPush, PriceAlertPush, InstockPush isimli classlar tanımlayınız.
+>WebPush class’ı send_push  isimli bir fonksiyona sahip olsun ve bu fonksiyon çağırıldığı zaman ‘Push gönderildi!’
yazısı gösterilsin.
 +>Bu class’lar WebPush classından miras alsın.Miras alan classlar ana classtan farklı olarak aşağıdaki değişkenlere
 sahip olsun:
+>discountPrice(price_info, discount_rate) - Bu method üründe yapılan indirimi hesaplayacak ve return ile geri
döndürecek. +>stockUpdate() - Bu method stock bilgisini güncelleyip return ile geri döndürecek.
+>>Örneğin
oluşturulan nesnenin stock bilgisi true ile false, false ise true yapacak. Bütün push çeşitlerinden nesne oluşturup,
methodlarını varsa kullanılmalı ve ana classta bulunan send_push methodu çağırılmalı.

"""


class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def sendPush(self):
        print(self.push_type, 'Push gönderildi!')


class TriggerPush(WebPush):
    trigger_page = "productDetail"


class BulkPush(WebPush):
    send_date = 1609783905


class SegmentPush(WebPush):
    segment_name = "last_visited"


class PriceAlertPush(WebPush):

    def discoutPrice(self, price_info, discount_rate):
        discounted_price = price_info - (price_info * discount_rate / 100)
        return discounted_price


class InstockPush(WebPush):

    def stockUpdate(self, stock_info):
        if stock_info == True:
            return False
        else:
            return True


trigger_push = TriggerPush("Mobile", True, 1, 1612201276, 1622569276, "tr_TR", "Trigger")
trigger_push.sendPush()

bulk_push = BulkPush("Mobile", True, 1, 1612201276, 1622569276, "tr_TR", "Bulk")
bulk_push.sendPush()

segment_push = SegmentPush("Desktop", True, 1, 1612201276, 1622569276, "tr_TR", "Segment")
segment_push.sendPush()

price_alert_push = PriceAlertPush("Desktop", True, 1, 1612201276, 1622569276, "tr_TR", "Price Alert")
price_alert_push.discoutPrice(200, 15)
price_alert_push.sendPush()

instock_push = InstockPush("Mobile", True, 1, 1612201276, 1622569276, "tr_TR", "Instock ")
instock_push.stockUpdate(False)
instock_push.sendPush()

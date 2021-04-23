"""
+> WebPush isimli bir class tanımlayınız. +>Platform, optin, global_frequency_capping, start_date, end_date,
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
    trigger_page: str

    def __init__(self, trigger_page, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    send_date: int

    def __init__(self, send_date, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class SegmentPush(WebPush):
    segment_name: str

    def __init__(self, segment_name, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

    def discountPrice(price_info, discount_rate):
        discounted_price = price_info - (price_info * discount_rate)
        print(discounted_price)
        return discounted_price


class PriceAlertPush(WebPush):
    price_info: int
    discount_rate: float

    def __init__(self, price_info, discount_rate, platform, optin, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.discount_rate = discount_rate
        self.price_info = price_info


class InstockPush(WebPush):
    stock_info: bool

    def __init__(self, stock_info, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self):
        if self.stock_info:
            self.stock_info = False
        else:
            self.stock_info = True


trigger_push = TriggerPush("product_page", "Mobile", True, 1, 1612201276, 1622569276, "tr_TR", "Trigger")
trigger_push.sendPush()

bulk_push = BulkPush(1260458952, "Mobile", True, 1, 1612201276, 1622569276, "tr_TR", "Bulk")
bulk_push.sendPush()

segment_push = SegmentPush("kadın", "Desktop", True, 1, 1612201276, 1622569276, "tr_TR", "Segment")
segment_push.sendPush()

price_alert_push = PriceAlertPush(40, 0.15, "Desktop", True, 1, 1612201276, 1622569276, "tr_TR", "Price Alert")
price_alert_push.sendPush()

instock_push = InstockPush(False, "Mobile", True, 1, 1612201276, 1622569276, "tr_TR", "Instock ")
instock_push.sendPush()

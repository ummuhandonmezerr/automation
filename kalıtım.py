class WebPush():
    def __init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform=Platform
        self.Optin=optin
        self.gfc=global_frequency_capping
        self.startdate=start_date
        self.enddate=end_date
        self.language=language
        self.pushtype=push_type
    def send_push(self):
        print('push gönderildi')

class TriggerPush(WebPush):
    def __init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type,trigger_page):
        WebPush.__init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.triggerpage=trigger_page

class BulkPush(WebPush): 
    def __init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type,send_date):
        WebPush.__init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.senddate=send_date

class SegmentPush(WebPush):
    def __init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type,segment_name):
        WebPush.__init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segmentname=segment_name

class PriceAlertPush(WebPush): 
    def __init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type,price_info,discount_rate):
        WebPush.__init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.priceinfo=price_info
        self.discountrate=discount_rate

    def discountPrice(self):
        return (self.price_info-((self.price_info*self.discount_rate)/100))

class InStockPushPush(WebPush): 
    def __init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type,stock_info):
        WebPush.__init__(self,Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stockinfo=stock_info
        
    def stockUpdate(self):
        return self.stock_info;True


a1=WebPush('web',True,1,6/10/21,8/10/21,'EN','web push')
a1.send_push()
a2=TriggerPush('web',True,2,7/10/21,11/10/21,'TR','trigger push','product')
a3=PriceAlertPush('web',True,3,8/10/21,10/10/21,'EN','price alert push',100,10)
a3.discountPrice()
a4=InStockPushPush('web',True,3,5/10/21,10/10/21,'EN','ın stock push',True)


a4.stockUpdate()
print(a1.platform + a1.Optin +a1.gfc + a1.startdate + a1.enddate + a1.pushtype)


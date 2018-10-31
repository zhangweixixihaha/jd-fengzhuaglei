#-*-coding:utf-8-*-
from util import firefoxutil,urlutil
import time
class JMain(object):

    def __init__(self):
        self.url=urlutil.URL()
        self.mainshopping=firefoxutil.startFireFox2()

        pass

    def OpenFire(self):
        self.mainshopping.startFireFox1(self.url.JD_LONGIN)

        pass

    def CloseFire(self):
        self.mainshopping.closeFireFox()

        pass

    def Shopping(self):
        # 查找空间输入用户名和密码
        self.mainshopping.ClickClassName("login-tab-r")
        # 查找空间 输入用户名密码
        self.mainshopping.FindID("loginname").send_keys("15510520530")
        self.mainshopping.FindID("nloginpwd").send_keys("zhangwei523")
        time.sleep(1)
        self.mainshopping.ClickId("loginsubmit")
        # 在输入框里面输入
        time.sleep(3)
        self.mainshopping.FindID("key").send_keys(u"裤子男")
        # 点击搜索
        self.mainshopping.FindClassName("button").click()
        time.sleep(3)
        # 选择品牌“花花公子”.根据标签定位一组元素点击第一个
        self.mainshopping.FindXPath("/html/body/div[6]/div[2]/div[1]/div[1]/div/div[2]/div[2]/ul/li[1]/a").click()
        # 滑动到要点击的地方（第1个）
        js = "var q=document.documentElement.scrollTop=100"
        self.mainshopping.driver.execute_script(js)
        # 获得当前窗口
        dq = self.mainshopping.driver.current_window_handle
        # 点击
        # self.mainshopping.FindClassNames("gl-item")[0].click()
        self.mainshopping.FindXPath(".//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
        time.sleep(5)
        # 获取所有窗口
        alle=self.mainshopping.driver.window_handles
        # 切换窗口
        for i in alle:
            if i!= dq:
                self.mainshopping.driver.switch_to_window(i)
        js = "var q=document.documentElement.scrollTop=350"
        self.mainshopping.driver.execute_script(js)
        # 选择灰色裤子
        self.mainshopping.FindXPath(".//*[@id='choose-attr-1']/div[2]/div[3]/a/img").click()
        time.sleep(2)
        # 选择xxl
        self.mainshopping.FindXPath("/html/body/div[8]/div/div[2]/div[4]/div[6]/div[3]/div[2]/div[4]/a").click()
        # 数量加一
        self.mainshopping.ClickClassName("btn-add")
        # self.mainshopping.FindXPath(".//*[@id='choose-btns']/div/div/a[2]").click()
        # 点击加入购物车
        # self.mainshopping.ClickId("InitCartUrl")
        self.mainshopping.FindXPath(".//*[@id='InitCartUrl']").click()
        # 获取购物车页面句柄
        gw = self.mainshopping.driver.current_window_handle
        # 进入购物车
        time.sleep(2)
        self.mainshopping.FindXPath(".//*[@id='GotoShoppingCart']").click()
        time.sleep(1)
        # # 获取所有句柄
        # allgw=self.mainshopping.driver.window_handles
        # for i in allgw:
        #     if i!=gw:
        #         self.mainshopping.driver.switch_to_window(i)
        # 点击去结算
        self.mainshopping.FindXPath(".//*[@id='cart-floatbar']/div/div/div/div[2]/div[4]/div[1]/div/div[1]/a/b").click()

       #  # 根据id切换到iframe上
       #  self.mainshopping.driver.switch_to_frame("dialogIframe")
       #  # 点击下拉
       #  self.mainshopping.FindXPath(".//*[@id='jd_area']/div[1]/b").click()
       #  # 选择朝阳去
       #  self.mainshopping.FindXPath("/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/ul/li[1]/a").click()
       #  # 选择五环到六环之间
       #  self.mainshopping.FindXPath("/html/body/div[2]/div[1]/div/div[2]/div[2]/div[3]/ul/li[3]/a").click()
       # # 输入收货人
       #  self.mainshopping.FindID("consignee_name").send_keys(u"收货人")
       #  # 输入详细地址
       #  self.mainshopping.FindID("consignee_address").send_keys(u"详细地址")
       #  # 输入手机号
       #  self.mainshopping.FindID("consignee_mobile").send_keys("13211111111")
       #  # 点击保存地址
       #  self.mainshopping.FindXPath("/html/body/div[2]/div[10]/div[1]/a/span").click()

        pass
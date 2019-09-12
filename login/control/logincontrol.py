#-*- coding:utf-8 -*-
from util import firefoxutil,urlutil
import time
import unittest
class loginCon(object):

    def __init__(self):
        self.URL = urlutil.URL()
        self.fire = firefoxutil.startFireFox2()

        pass
    # 点击账号登录
    # def ClickAccout(self,cls):
    #     self.firefox.Clickclass(cls)
    #     pass

    def openfix(self):
        self.fire.startFireFox1(self.URL.JD_LONGIN)
        pass
    def closefix(self):
        self.fire.closeFireFox()

        pass

    def res(self):
        self.fire.driver.refresh()

        pass
    def Sendkeys(self,self1):
        # self.ClickAccout(cls)
        # 查找空间输入用户名和密码
        self.fire.ClickClassName("login-tab-r")
        # 查找空间 输入用户名密码
        self.fire.FindID("loginname").send_keys("")
        self.fire.FindID("nloginpwd").send_keys("")
        self.fire.ClickId("loginsubmit")
        # 查找 信息进行断言
        message = self.fire.FindClassName("msg-wrap").text
        self1.assertEqual(message, u"请输入账户名和密码")

        pass

    def SenkeysOk(self,self1):
        # 查找空间输入用户名和密码
        self.fire.ClickClassName("login-tab-r")
        # 查找空间 输入用户名密码
        self.fire.FindID("loginname").send_keys("15510520530")
        self.fire.FindID("nloginpwd").send_keys("zhangwei523")
        time.sleep(5)
        self.fire.ClickId("loginsubmit")
        time.sleep(5)
        titile=self.fire.driver.title
        
        self1.assertEqual(titile,u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
        js = "var q=document.documentElement.scrollTop=250"
        self.fire.driver.execute_script(js)
        time.sleep(3)
        self.fire.FindClassNames("slider_indicators_btn")[6].click()
        time.sleep(2)
        self.fire.FindXPath(".//*[@id='J_focus']/div/div/div[1]/div/li[7]/a/img").click()
        time.sleep(5)




        pass
if __name__ == '__main__':
    unittest.main()
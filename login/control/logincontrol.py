#-*- coding:utf-8 -*-
class loginCon(object):
    def __init__(self,fire):
        self.fire=fire
        pass
    # 点击账号登录
    # def ClickAccout(self,cls):
    #     self.firefox.Clickclass(cls)
    #     pass
    def Sendkeys(self,username,password,self1):
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

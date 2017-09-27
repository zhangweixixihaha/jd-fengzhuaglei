#-*- coding:utf-8 -*-
import unittest
from util import firefoxutil,urlutil
from  login.control import logincontrol
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 实例化类
        self.fire=firefoxutil.startFireFox2()
        # 实例化url类
        self.URL=urlutil.URL()
        self.contro=logincontrol.loginCon(self.fire)
        pass
    def setUp(self):
        # 打开京东登录页面
        self.fire.startFireFox1(self.URL.JD_LONGIN)

        pass
    def tearDown(self):
        # 关闭页面
        self.fire.closeFireFox()
        pass
    @classmethod
    def tearDownClass(self):
        pass
    def test_up(self):

        self.contro.Sendkeys("","",self)


        pass
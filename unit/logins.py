# -*- coding:utf-8 -*-
import unittest
from  login.control import logincontrol


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.con = logincontrol.loginCon()

        pass


def setUp(self):
    # 打开京东登录页面
    self.con.openfix()

    pass


def tearDown(self):
    # 关闭页面
    self.con.closefix()


    pass


def test_up(self):
    u"""登陆失败"""
    self.con.Sendkeys(self)

    

    pass


def test_Ok(self):
    u"""登陆成功"""
    self.con.SenkeysOk(self)

    pass

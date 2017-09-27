#-*- coding:utf-8 -*-
import unittest
from unit import  logins
import HTMLTestRunner
unit=unittest.TestSuite()
unit.addTest(unittest.makeSuite(logins.Login))
filename='C:/Users/Administrator/Desktop/123.html'
paths=open(filename,'wb')
runnerr=HTMLTestRunner.HTMLTestRunner(stream=paths,title=u'用例',description=u'京东用例')
runnerr.run(unit)

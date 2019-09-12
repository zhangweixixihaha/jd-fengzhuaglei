#-*- coding:utf-8 -*-
import unittest
from unit import logins,mains
import HTMLTestRunner
import os
unit=unittest.TestSuite()
unit.addTest(unittest.makeSuite(logins.Login))
# unit.addTest(unittest.makeSuite(mains.Maines))
filename=os.getcwd()+"/jd.html"
paths=open(filename,'wb')
runnerr=HTMLTestRunner.HTMLTestRunner(stream=paths,title=u'用例',description=u'京东用例')
runnerr.run(unit)
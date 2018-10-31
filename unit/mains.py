#-*-coding:utf-8-*-
import unittest
from mainz import jdmain
class Maines(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.jd=jdmain.JMain()


        pass

    def setUp(self):
        self.jd.OpenFire()

        pass

    def tearDown(self):
        self.jd.CloseFire()

        pass

    def test_mainse(self):
        self.jd.Shopping()


        pass
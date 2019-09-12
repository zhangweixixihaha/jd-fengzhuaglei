#-*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 定义一个类继承object
class startFireFox2(object):
    # 打开浏览器的方法
    def startFireFox1(self,url):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        # 设置等待时间


        pass
    # 关闭浏览器的方法
    def closeFireFox(self):
        self.driver.quit()

        pass
    #静止休眠
    def TimeSleep(self,number):
        time.sleep(number)


    #隐士休眠
    def ImplaySleep(self,number):
        self.driver.implicitly_wait(number)
        pass
    # 显示休眠
    def WebWait(self,message):
        try:

            text=(By.LINK_TEXT,message)
            WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(text))
            return self.driver.find_element_by_link_text(message)

        except Exception:
            return self.driver.find_element_by_link_text(message)



    # 获取控件的方法
    def FindID(self,ID):
        try:
            ids=(By.ID,ID)
            WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(ids))
            return self.driver.find_element_by_id(ID)
        except Exception:
            return self.driver.find_element_by_id(ID)

    def FindIDs(self, ID):
        try:
            ids = (By.ID, ID)

            WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(ids))
            return self.driver.find_elements_by_id(ID)
        except Exception:
            return self.driver.find_elements_by_id(ID)


    # def FindLink(self, ID):
    #     try:
    #         ids = (By.LINK_TEXT, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_element_by_link_text(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindName(self, ID):
    #     try:
    #         ids = (By.NAME, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_element_by_name(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    def FindXPath(self, ID):
        try:
            ids = (By.XPATH, ID)
            WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(ids))
            return self.driver.find_element_by_xpath(ID)
        except Exception:

            return self.driver.find_element_by_xpath(ID)
    #
    #
    # def FindPres(self, ID):
    #     try:
    #         ids = (By.PARTIAL_LINK_TEXT, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_element_by_partial_link_text(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindCss(self, ID):
    #     try:
    #         ids = (By.CSS_SELECTOR, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_element_by_css_selector(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindTagName(self, ID):
    #     try:
    #         ids = (By.TAG_NAME, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_element_by_tag_name(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    def FindClassName(self, ID):
        try:
            ids = (By.CLASS_NAME, ID)
            WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(ids))
            return self.driver.find_element_by_class_name(ID)
        except Exception:
            return self.driver.find_element_by_class_name(ID)

    def FindClassNames(self, ID):
        try:
            ids = (By.CLASS_NAME, ID)
            WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(ids))
            return self.driver.find_elements_by_class_name(ID)
        except Exception:
            return self.driver.find_elements_by_class_name(ID)



    #
    #
    #
    #     # 获取控件的方法
    #
    # def FindIDs(self, ID):
    #     try:
    #         ids = (By.ID, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_elements_by_id(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindLinks(self, ID):
    #     try:
    #         ids = (By.LINK_TEXT, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_elements_by_link_text(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindNames(self, ID):
    #     try:
    #         ids = (By.NAME, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_elements_by_name(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindXPaths(self, ID):
    #     try:
    #         ids = (By.XPATH, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_elements_by_xpath(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindPreses(self, ID):
    #     try:
    #         ids = (By.PARTIAL_LINK_TEXT, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_elements_by_partial_link_text(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    # def FindCsss(self, ID):
    #     try:
    #         ids = (By.CSS_SELECTOR, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_elements_by_css_selector(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    #
    def FindTagNames(self, ID):
        try:
            ids = (By.TAG_NAME, ID)
            WebDriverWait(self.driver,).until(EC.presence_of_all_elements_located(ids))
            return self.driver.find_elements_by_tag_name(ID)
        except Exception:

            return self.driver.find_elements_by_tag_name(ID)


    # def FindClassNamess(self, ID):
    #     try:
    #         ids = (By.CLASS_NAME, ID)
    #         WebDriverWait(self.driver, ENUMS.TWENTY_TIME, ENUMS.ZONE_TIME).until(
    #             EC.presence_of_all_elements_located(ids))
    #         return self.driver.find_elements_by_class_name(ID)
    #     except Exception:
    #
    #         return Exception
    #     pass
    def ClickId(self,ID):
        self.FindID(ID).click()
        self.TimeSleep(2)
        pass
    def ClickClassName(self,cls):
        self.FindClassName(cls).click()
        self.TimeSleep(2)
        
        pass

    def GetTitlee(self):

        return self.driver.title

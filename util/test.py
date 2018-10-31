#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Firefox()
# 打开百度网页
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(3)
# 选择设置按钮
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[8]").click()
# 选择搜索设置
driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[1]").click()
# 定位到下拉框
s=driver.find_element_by_id("nr")
# 使用select的方法直接定位到下拉框的内容点击
Select(s).select_by_visible_text("每页显示20条")
s.click()
# 点击保存设置
driver.find_element_by_link_text("保存设置").click()
# 切换到alert上面
t=driver.switch_to_alert()
print t.text
time.sleep(2)
# 点击确定
t.accept()
time.sleep(5)


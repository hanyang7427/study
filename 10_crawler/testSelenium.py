# -*- coding:utf-8 -*-
# 导入webdriver
from selenium import webdriver

# 想调用键盘按键操作
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定PhantomJS浏览器
# 'phantomjs' executable needs to be in PATH.
driver = webdriver.PhantomJS()

# 获取网页title信息
driver.get("http://www.bing.com")
print(driver.title)

# 获取网页title信息
data = driver.find_element_by_id("scpl1").text
print(data)

# 打开bing做一个搜索的操作，同时截图
driver.find_element_by_id("sb_form_q").send_keys("Python")
driver.find_element_by_id("sb_form_go").click()
driver.save_screenshot("python.png")

# 关闭浏览器
driver.quit()
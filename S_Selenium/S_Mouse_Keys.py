# coding:utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://www.baidu.com"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("selenium")

driver.find_element_by_id("kw").text
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").size
driver.find_element_by_id("kw").is_displayed()

time.sleep(3)
ele1 = driver.find_element(By.ID, "su")
ActionChains(driver).context_click(ele1).send_keys(Keys.CONTROL, "R")

"""
回车键 Keys.ENTER
删除键 Keys.BACK_SPACE
空格键 Keys.SPACE
制表键 Keys.TAB
回退键 Keys.ESCAPE
刷新键 Keys.F5
send_keys(Keys.CONTROL,'a') 　　#全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 　　#复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 　　#剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 　　#粘贴（Ctrl+V）
"""

# 悬浮操作
ele = driver.find_element(By.LINK_TEXT, "设置")
ActionChains(driver).move_to_element(ele).perform()

driver.find_element_by_partial_link_text("搜索设置").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id=\"wrapper\"]/div[7]/span").click()






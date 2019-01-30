# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

import time

url = "file://E:/PyS/S_Selenium/1.html"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(1)

"""
# upload 上传文件操作
# 1.定位元素
upload = driver.find_element_by_xpath("/html/body/center/p[1]/table/tbody/tr[1]/td[2]/input")
# 2.上传文档
upload.send_keys("E:/PyS/S_Selenium/1.html")

time.sleep(1)
# alert 操作
# 1.定位元素并进行单击操作
click_alert = driver.find_element_by_name("alterbutton")
click_alert.click()
time.sleep(1)
# 2.切换到弹出窗体
alert_btn = driver.switch_to.alert
print(alert_btn.text)
# 3.点击弹出窗上的确认按钮
alert_btn.accept()
time.sleep(1)

# prompt 操作
# 1.定位元素并进行单击操作
click_prompt = driver.find_element_by_name("promptbutton")
click_prompt.click()
time.sleep(1)
# 2.切换到弹出窗体
prompt_btn = driver.switch_to.alert
print(prompt_btn.text)
# 3.在弹出窗体中输入文字
prompt_btn.send_keys("I Love Selenium")
# 4.点击弹出窗上的确认按钮
prompt_btn.accept()
time.sleep(1)
prompt_btn.accept()
time.sleep(1)

# confirm 操作
# 1.定位元素并进行单击操作
click_confirm = driver.find_element_by_name("confirmbutton")
click_confirm.click()
# 2.切换到弹出窗体
confirm_btn = driver.switch_to.alert
# 3.点击弹出窗上的确认按钮
confirm_btn.accept()
time.sleep(3)
confirm_btn.accept()
time.sleep(3)

# 1.定位元素并进行单击操作
click_confirm = driver.find_element_by_name("confirmbutton")
click_confirm.click()
# 2.切换到弹出窗体
confirm_btn = driver.switch_to.alert
# 3.点击弹出窗上的取消按钮
confirm_btn.dismiss()
time.sleep(3)
confirm_btn.accept()
time.sleep(3)

# 1.定位下拉菜单元素位置
select_btn = driver.find_element_by_id("Selector")
# 2.1.通过Index定位  Index从0开始
Select(select_btn).select_by_index(5)
time.sleep(3)
# 2.2.通过option中values属性值定位
Select(select_btn).select_by_value("peach")
time.sleep(3)
# 2.3.通过文本值定位
Select(select_btn).select_by_visible_text("香蕉")
time.sleep(3)
"""

# 单选框操作(RadioBox)
# 1.定位单选框的位置
Baidu_Radio = driver.find_element(by="class name", value="Baidu")
Ali_Radio = driver.find_element(by="class name", value="AliBaBa")
Tencent_Radio = driver.find_element(by="class name", value="Tencent")
Mi_Radio = driver.find_element(by="class name", value="Mi")
# 2.判断单选框是否可用，是否已被选中
if Mi_Radio.is_enabled():
    Mi_Radio.click()
elif Tencent_Radio.is_enabled():
    if Tencent_Radio.is_selected():
        # 3.若可用且未选中，指定单击操作
        Baidu_Radio.click()
    else:
        Tencent_Radio.click()
time.sleep(3)

# 复选框操作(CheckBox)
Check_Box = driver.find_elements(By.ID, "checkbox")
print(Check_Box)
for cb in Check_Box:
    cb.click()
    time.sleep(3)

time.sleep(3)
driver.quit()

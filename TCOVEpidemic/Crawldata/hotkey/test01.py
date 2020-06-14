# coding: utf-8
"""
@Time    : 2020/5/28 2:25
@Author  : VillageTony
@FileName: test01.py
@Software: PyCharm
@Blog    ：https://www.diaoyc.cn/
"""

import time
from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\Tony\PycharmProjects\Epidemic\app\hotkey\chromedriver.exe")
driver.get("http://www.baidu.com")
print(driver.title)
time.sleep(5)
driver.quit()
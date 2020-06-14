# coding: utf-8
"""
@Time    : 2020/5/28 0:57
@Author  : VillageTony
@FileName: test_hotkey.py
@Software: PyCharm
@Blog    ：https://www.diaoyc.cn/
"""
# import requests

# res = requests.get(url)
# print(res)
# print(res.text)

# from selenium.webdriver import Chrome,ChromeOptions
#
# browser = Chrome()

from selenium import webdriver
url = 'https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1'
option = webdriver.ChromeOptions()
option.add_argument("--headless")  # 通过ChromeOptions设置隐藏浏览器
option.add_argument('--no-sandbox') # 在Linux上禁用浏览器沙盒
browser = webdriver.Chrome(options=option)

browser.get(url)
# print(browser.page_source)
browser.implicitly_wait(3)  # 隐式等待

# # 显示等待
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(browser, 10, poll_frequency=0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.ID, 's_mp')))

check_more_btn = browser.find_element_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/div')
check_more_btn.click()

hotels = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/a/div/span[2]')
print(type(hotels))
hotkeys = []
for hotel in hotels:
    print(hotel.text)
    hotkeys.append(hotel.text)

print(hotkeys)


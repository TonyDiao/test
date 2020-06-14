# coding: utf-8
"""
@Time    : 2020/5/28 1:36
@Author  : VillageTony
@FileName: HotKey.py
@Software: PyCharm
@Blog    ：https://www.diaoyc.cn/
"""

from selenium import webdriver


class HotKey:
    def __init__(self):
        """
        初始化selenium参数
        """
        url = 'https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1'
        self.option = webdriver.ChromeOptions()
        self.option.add_argument("--headless")  # 通过ChromeOptions设置隐藏浏览器
        self.option.add_argument('--no-sandbox')  # 在Linux上禁用浏览器沙盒
        # self.browser = webdriver.Chrome(options=self.option)
        driver_path = r'C:\Users\Tony\PycharmProjects\Epidemic\app\hotkey\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path=driver_path, options=self.option)
        self.browser.get(url)
        self.browser.implicitly_wait(3)  # 隐式等待

    def get_baidu_hot(self):
        """
        元素定位
        :return:
        """
        hotkeys = [] # 存放热词
        check_more_btn = self.browser.find_element_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/div')
        check_more_btn.click()

        hotels = self.browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/a/div/span[2]')
        for hotel in hotels:
            hotkeys.append(hotel.text)

        return hotkeys

# coding: utf-8
"""
@Time    : 2020/5/27 22:23
@Author  : VillageTony
@FileName: TencentData.py
@Software: PyCharm
@Blog    ：https://www.diaoyc.cn/
"""
import requests
import json
import time

"""
封装获取数据的方法

腾讯接口返回数据结构如下：
lastUpdateTime  最后更新的时间
chinaTotal 总数
chinaDayList  历史记录
chinaDayAddList  历史新增记录
areaTree:           # areaTree[0] 中国数据
    -name   
    -today              
    -total              
    -children:   # 省级数据 列表
        -name
        -today              
        -total  
        -children:         # 市级数据 列表
                -name
                -today              
                -total                  
"""


class TencentData:
    @classmethod
    def common(self, url):
        """
        根据传入的链接返回数据
        :param url:
        :return:
        """
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36"
        }
        r = requests.get(url, headers)
        res = json.loads(r.text)  # json字符串转字典
        data_all = json.loads(res['data'])
        return data_all

    @classmethod
    def get_tencent_data_history(self):
        """
        获取腾讯的新冠疫情历史数据
        :return: 返回历史数据
        """
        url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
        data_all = self.common(url)

        history = {}  # 历史数据
        for i in data_all['chinaDayList']:
            ds = '2020.' + i['date']
            tup = time.strptime(ds, "%Y.%m.%d")
            ds = time.strftime("%Y-%m-%d", tup)  # 格式化时间否则存到数据库时会报错
            confirm = i['confirm']  # 确诊
            suspect = i['suspect']  # 疑似
            heal = i['heal']  # 治愈
            dead = i['dead']  # 死亡
            history[ds] = {'confirm': confirm, 'suspect': suspect, 'heal': heal, 'dead': dead}

        for i in data_all['chinaDayAddList']:  # 历史新增记录
            ds = '2020.' + i['date']
            tup = time.strptime(ds, "%Y.%m.%d")
            ds = time.strftime("%Y-%m-%d", tup)
            confirm = i['confirm']
            suspect = i['suspect']
            heal = i['heal']
            dead = i['dead']
            history[ds].update({'confirm_add': confirm, 'suspect_add': suspect, 'heal_add': heal, 'dead_add': dead})
        return history

    @classmethod
    def get_tencent_data_details(self):
        """
        :return: 返回当日详情数据
        """
        url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
        data_all = self.common(url)

        details = []  # 当日详细数据
        update_time = data_all['lastUpdateTime']  # 最后更新的时间
        data_country = data_all['areaTree']  # 国家
        data_province = data_country[0]['children']  # 中国各省
        for pro_infos in data_province:
            province = pro_infos['name']  # 省名
            for city_infos in pro_infos['children']:
                city = city_infos['name']
                confirm = city_infos['total']['confirm']
                confirm_add = city_infos['today']['confirm']
                heal = city_infos['total']['heal']
                dead = city_infos['total']['dead']
                details.append([update_time, province, city, confirm, confirm_add, heal, dead])
        return details

# 国外数据接口：https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign

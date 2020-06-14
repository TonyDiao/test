# coding: utf-8
"""
@Time    : 2020/5/27 23:36
@Author  : VillageTony
@FileName: db.py
@Software: PyCharm
@Blog    ：https://www.diaoyc.cn/
"""
import pymysql
import time
import traceback  # 追踪异常
from Crawldata.getdata.TencentData import TencentData
from Crawldata.hotkey.HotKey import HotKey


class DbOperation:
    """
    操作数据库类
    """

    def get_connect(self):
        """
        获取数据库链接对象
        :return:
        """
        # 获取数据库连接对象
        conn = pymysql.connect(host='localhost', port=3306,
                               user='root', passwd='root',
                               database='cov', charset='utf8')

        # conn = pymysql.connect(host='localhost', port=3306,
        #                        user='root', password='root',
        #                        database='cov', charset='utf8',
        #                        cursorclass=pymysql.cursors.DictCursor)
        '''
        cursorclass=pymysql.cursors.DictCursor
        表示设置游标类型为字典
        '''
        return conn

    def update_details(self):
        """
        更新details表
        :return:
        """
        conn = self.get_connect()
        try:
            li = TencentData.get_tencent_data_details()  # 返回值为一个列表
            sql = 'insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values (%s,%s,%s,%s,%s,%s,%s)'
            sql_query = 'select %s=(select update_time from details order by id desc limit 1)'  # 对比当前最大时间戳
            cursor = conn.cursor()
            cursor.execute(sql_query, li[0][0])
            if not cursor.fetchone()[0]:
                print(f'{time.asctime()}开始更新数据......')
                for item in li:
                    cursor.execute(sql, item)
                conn.commit()  # 事务提交
                print(f'{time.asctime()}更新数据完毕......')
            else:
                print(f'{time.asctime()}已是最新数据！')
        except pymysql.MySQLError as err:
            print(err)
            traceback.print_exc()
            conn.rollback()  # 出现异常时 事务回滚
        finally:
            cursor.close()
            conn.close()

    def inset_history(self):
        """
        插入历史数据
        :return:
        """
        conn = self.get_connect()
        try:
            dict = TencentData.get_tencent_data_history()  # 返回一个字典
            print(f'{time.asctime()}开始插入历史数据......')
            sql = 'insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            for k, v in dict.items():
                with conn.cursor() as cursor:
                    cursor.execute(sql, [k,
                                         v.get('confirm'), v.get('confirm_add'),
                                         v.get('suspect'), v.get('suspect_add'),
                                         v.get('heal'), v.get('heal_add'),
                                         v.get('dead'), v.get('dead_add')
                                         ])
            conn.commit()
            print(f'{time.asctime()}历史数据插入完成......')
        except pymysql.MySQLError as err:
            print(err)
            traceback.print_exc()
            conn.rollback()
        finally:
            conn.close()

    def update_history(self):
        """
        更新历史数据
        :return:
        """
        conn = self.get_connect()
        try:
            dict = TencentData.get_tencent_data_history()  # 返回一个字典
            print(f'{time.asctime()}开始更新历史数据......')
            sql = 'insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            sql_query = 'select confirm from history where ds=%s'
            cursor = conn.cursor()
            for k, v in dict.items():
                if not cursor.execute(sql_query, k):
                    cursor.execute(sql, [k,
                                         v.get('confirm'), v.get('confirm_add'),
                                         v.get('suspect'), v.get('suspect_add'),
                                         v.get('heal'), v.get('heal_add'),
                                         v.get('dead'), v.get('dead_add')
                                         ])
            conn.commit()
            cursor.close()
            print(f'{time.asctime()}历史数据更新完成......')
        except pymysql.MySQLError as err:
            print(err)
            traceback.print_exc()
            conn.rollback()
        finally:
            conn.close()

    def update_hotsearch(self):
        """
        将热搜词存放到数据库
        :return:
        """
        conn = self.get_connect()
        try:
            context = HotKey().get_baidu_hot()  # 返回一个字典
            print(f'{time.asctime()}开始更新热搜词数据......')
            sql = 'insert into hotsearch(dt,content) values (%s,%s)'
            ts = time.strftime("%Y-%m-%d %X")
            with conn.cursor() as cursor:
                for i in context:
                    cursor.execute(sql, (ts, i))
                conn.commit()
            print(f'{time.asctime()}热搜词数据更新完成......')
        except pymysql.MySQLError as err:
            print(err)
            traceback.print_exc()
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


# DbOperation().inset_history()
DbOperation().update_hotsearch()

# coding: utf-8
"""
@Time    : 2020/5/27 23:27
@Author  : VillageTony
@FileName: test_db.py
@Software: PyCharm
@Blog    ：https://www.diaoyc.cn/
"""
import pymysql
import traceback # 追踪异常

from .DbOperation import DbOperation

# # 配置数据库连接
# conn = pymysql.connect(host='localhost',
#                        port=3306,
#                        user='root',
#                        password='root',
#                        db='cov')
#  # 创建游标，默认是元组形式
# cursor = conn.cursor()
# sql = 'select * from history'
# cursor.execute(sql)
#
# # conn.commit() # 提交事务
# res = cursor.fetchall()
# print(res)
# cursor.close()
# conn.close()


DbOperation().inset_history()
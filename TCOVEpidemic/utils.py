# coding: utf-8
"""
@Time    : 2020/5/28 4:12
@Author  : VillageTony
@FileName: utils.py
@Software: PyCharm
@Blog    ：https://www.diaoyc.cn/
"""
import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format('年', '月', '日')


def get_connect():
    """
    获取数据库链接对象
    :return:
    """
    # 获取数据库连接对象
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='root',
                           database='cov', charset='utf8')
    return conn


def close_conn(conn,cursor):
    """
    关闭数据库连接
    :param conn:
    :param cursor:
    :return:
    """
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    """
    通用查询
    :param sql:
    :param args:
    :return:
    """
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res


def get_c1_data():
    """
    返回大屏div id=center1的数据
    :return:
    """
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal),sum(dead) " \
          "from details " \
          "where " \
          "update_time = " \
          "(select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    return res[0]

def get_c2_data():
    """
    返回大屏div id=center2的数据
    :return:
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select province, sum(confirm) from details where update_time=(select update_time from details order by update_time DESC limit 1) group by province"

    res = query(sql)
    return res

def get_l1_data():
    """
    获取每天历史累计数据
    :return:
    """
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res

def get_l2_data():
    """
    获取全国新增趋势
    :return:
    """
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res

def get_r1_data():
    """
    返回非湖北地区城市确诊人数排名
    :return:
    """
    sql = "select city,confirm from (select city,confirm from details where update_time=(select update_time from details order by update_time desc limit 1)and province not in ('地区待确认','湖北','北京','上海','天津','重庆') union all select province as city,sum(confirm) as confirm from details where update_time = (select update_time from details order by update_time desc limit 1) and province in ('北京','上海','天津','重庆') group by province) as a  order by confirm desc limit 5"
    res = query(sql)
    return res

def get_r2_data():
    """
    返回最近20条热搜
    :return:
    """
    sql = "select content from hotsearch order by id limit 20"
    res = query(sql)
    return res

if __name__ == '__main__':
    # print(get_c1_data())
    # print(get_c1_data()[0])
    # print(get_c2_data())
    # print(get_l1_data())
    print(get_r1_data())
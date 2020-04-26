# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 10:46
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : DB_Handle.py
# @Software: PyCharm

"""
=== 数据库操作 ===
=== MySqlHandle: 封装MySql数据库操作
=== SqliteHandle：封装sqlite数据库操作
=== MongoDBHandle：封装mongodb数据库操作
=== RedisHandle：封装redis数据库操作
"""

import sqlite3

import pymysql

from common.Conf_Handle import yh

# 读取mysql数据库配置信息
mysql_data = yh.get_data("mysql")


class MySqlHandle(object):
    """封装MySql数据库操作"""

    def __init__(self):
        # 创建数据库连接
        self.con = pymysql.connect(host=mysql_data["host"],
                                   user=mysql_data["user"],
                                   password=mysql_data["password"],
                                   port=mysql_data["port"],
                                   database=mysql_data["database"],
                                   charset='utf8')
        # 创建游标
        self.cur = self.con.cursor()

    def find_one(self, sql) -> tuple:
        """
        查找返回第一条数据
        :param sql:
        :return:
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self, sql) -> tuple:
        """
        查找返回所有数据
        :param sql:
        :return:
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def count(self, sql) -> int:
        """
        返回数据条数
        :param sql:
        :return:
        """
        self.con.commit()
        return self.cur.execute(sql)

    def close(self):
        """关闭游标对象和断开连接"""
        self.cur.close()
        self.con.close()


class SqliteHandle(object):
    """封装sqlite数据库操作"""

    def __init__(self, db_path):
        self.db_path = db_path

    def __open(self):
        # 连接数据库
        self.con = sqlite3.connect(self.db_path)
        # 创建游标
        self.cur = self.con.cursor()

    def __close(self):
        """关闭连接"""
        self.cur.close()
        self.con.close()

    def select_tab_name(self):
        """获取数据库中的所有表名"""
        self.__open()
        """查询所有的数据库名称"""
        self.cur.execute("select name from sqlite_master where type='table'")
        tab_name = self.cur.fetchall()
        tab_name = [line[0] for line in tab_name]
        return tab_name

    def select_tab_title(self, tab_name):
        """
        获取表的列名（字段名）
        :param tab_name:
        :return: col_names列表,每个表的字段名集为一个元组
        """
        self.__open()
        self.cur.execute('pragma table_info({})'.format(tab_name))
        col_name = self.cur.fetchall()
        col_name = [x[1] for x in col_name]
        col_name = tuple(col_name)
        self.__close()
        return col_name

    def select_tab_data(self, tab_name):
        """
        获取表的数据
        :param tab_name: 表名
        :return: 列表
        """
        self.__open()
        self.cur.execute("select * from {}".format(tab_name))
        datas = self.cur.fetchall()
        self.__close()
        col_name = self.select_tab_title(tab_name)
        return [dict(zip(col_name, data)) for data in datas]

    def write_data(self, tab_name, col_name, id, value):
        """
        写入数据
        :param tab_name: 数据库名字
        :param col_name: 列名
        :param id: id（通过id去修改）
        :param value: 修改的值
        """""
        self.__open()
        self.cur.execute(
            f"UPDATE {tab_name} SET {col_name}=? WHERE id=?", (value, id))
        self.con.commit()
        self.__close()


class MongoDBHandle(object):
    """封装mongodb数据库操作
    TODO: mongodb数据库操作-暂未封装
    """
    pass


class RedisHandle(object):
    """封装redis数据库操作
    TODO: redis数据库操作-暂未封装
    """
    pass


if __name__ == '__main__':
    # conn = pymysql.Connect(
    #     host="127.0.0.1",
    #     user="root",
    #     password="123456",
    #     database="py24",
    #     port=3306,
    #     charset="utf8")
    # cur = conn.cursor()
    sql = "select * from user"
    # cur.execute(sql)
    # c = cur.fetchall()
    # print(c)
    mh = MySqlHandle()
    data = mh.count(sql)
    print(data, type(data))

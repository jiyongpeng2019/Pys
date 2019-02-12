# coding:utf-8


import pymssql


def open_conn():
    server_name = "localhost"
    user_name = "sa"
    password_name = "123456"
    database_name = "TaskTracker"

    connection = pymssql.connect(host=server_name, user=user_name,password=password_name, database=database_name)
    # connection = pymssql.connect(server_name, user_name, password_name, database_name)
    cur = connection.cursor()

    if not cur:
        raise Exception("数据库连接失败")
    else:
        print("数据库连接成功")

    return connection, cur


def create_table(connection,cur):
    exist_sql = """if OBJECT_ID('person', 'U') IS NOT NULL 
                  DROP TABLE person"""
    create_sql = """CREATE TABLE person(id INT NOT NULL, name varchar(100), score INT NOT NULL)"""

    cur.execute(exist_sql)
    cur.execute(create_sql)
    connection.commit()


def insert_value(connection, cur):
    insert_sql = "insert into person(id, name, score) values('1', '1', '1')"
    inserts_sql = "insert into person(id, name, score) values(2, '2', '2'),(3, '3', 3)"
    cur.execute(insert_sql)
    cur.execute(inserts_sql)
    connection.commit()


def select_value(connection, cur):
    select_sql = "select * from person where id in ( 1, 2, 3)"
    cur.execute(select_sql)

    # row = cur.fetchone()
    # rows = cur.fetchall()
    # print(rows)
    for r in cur:
        print(r)


def delete_value(connection, cur):
    delete_sql = "delete from person where id = 3"
    cur.execute(delete_sql)
    connection.commit()


def update_value(connection, cur):
    update_sql = "update person set name = 'jyp' where id = 2"
    cur.execute(update_sql)
    connection.commit()


def close_conn(connection):
    connection.close()


if __name__ == "__main__":
    connection, cur = open_conn()
    create_table(connection, cur)
    insert_value(connection, cur)
    print("删除操作前查询")
    select_value(connection, cur)
    delete_value(connection, cur)
    print("删除操作后查询")
    select_value(connection, cur)
    update_value(connection, cur)
    print("更新后查询")
    select_value(connection, cur)
    close_conn(connection)


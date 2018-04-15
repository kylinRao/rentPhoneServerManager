# coding=utf-8
#!/usr/bin/env python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = './house.db'
conn = sqlite3.connect(DATABASE)


# 创建表格、插入数据
@app.before_first_request
def create_db():
    # 连接
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    with open('v1.0.sql', 'r') as f:
        c.executescript(f.read());

    # 提交！！！
    conn.commit()
    # 关闭
    conn.close()


if __name__ == '__main__':
    create_db()

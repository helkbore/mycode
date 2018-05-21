import sqlite3

conn = sqlite3.connect('E:\\备份\\sqlite\\spiders.db')
cursor = conn.cursor()
conn.commit()
conn.close()
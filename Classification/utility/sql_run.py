#!/usr/bin/python
# -*- coding: utf-8
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",
    port=3309,
    user="essayrater",
    passwd="Spunefr7",
    db="essayrater",
    charset='utf8')

cursor = db.cursor()

print cursor

f = open('/home/oleksandr/Documents/uuser.dump', 'w')

data = [1]
pos = 0
while len(data) > 0:
    sql = 'select id, email, customFields from uuser where customFields like \'%genre%\' limit ' + str(pos) + ', 100000'
    print sql

    cursor.execute(sql)

    data =  cursor.fetchall()

    for rec in data:
        try:
            f.write(str(rec)+ '\n')
        except UnicodeTranslateError:
            print rec[0], rec[1], rec[2]

    pos += 100000

    print pos

f.close()
db.close()
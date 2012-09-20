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

sql = """
select * from uuser;
"""
#select registrationDate, device_session.start, device_session.checkedChars, uuser.email from uuser, device_session
#    where
#        device_session.user_id = uuser.id and
#        uuser.email='korobov.alex@gmail.com' and
#        device_session.checkedChars > 0
#        ;
#"""

f = open('/home/oleksandr/Documents/uuser_witn_anonymous.dump', 'w')

data = [1]
pos = 0
while len(data) > 0:
    # select count(*) from uuser where email not like '%anonymous%'
    sql = 'select id, email, customFields from uuser where customFields like \'%genre%\' limit ' + str(pos) + ', 100000'
    print sql

    cursor.execute(sql)

    data =  cursor.fetchall()

    for rec in data:
        # print rec
        try:
            #f.write('id=' + str(rec[0]) + ' e=' + str(rec[1]) + ' cf=' + str(rec[2]) + '\n')
            f.write(str(rec)+ '\n')
        except UnicodeTranslateError:
            print rec[0], rec[1], rec[2]

    pos += 100000

    print pos

f.close()
db.close()
# -*- coding: utf-8 -*-
import re
import pymysql
#数据库连接信息
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='kun123567',
    db='patent_neu',
    charset='utf8'
)

# 获取游标
cursor = conn.cursor()
print(conn)
print(cursor)

#for i in range(1, 755):
for i in range(1, 755):
    # f = open("patent1.html", 'rb').read() #二进制方式打开，读入比特流
    f1 = open("/Users/kun/Desktop/patent_neu/patent_html/patent" + str(i) + ".html", 'rb').read()
    s = f1.decode() #解码

    s = s.replace("&lt;FONT&gt;东北大学&lt", "东北大学")
    s = s.replace("/FONT&gt;", ";")
    s = s.replace("东北大学;;;", "东北大学;")
    s = s.replace("东北大学;,", "东北大学,")
    s = s.replace("东北大学;;", "东北大学,")
    s = s.replace("东北大学,", "东北大学;")
    s = s.replace("辽宁省沈阳市和平区文化路3号巷11号;\"", "辽宁省沈阳市和平区文化路3号巷11号")
    s = s.replace('s=""',"")
    s = s.replace('of=""', "")
    s = s.replace('high=""', "")
    s = s.replace('speed=""', "")
    s = s.replace('railway=""', "")
    s = s.replace('fluidization=""', "")
    s = s.replace('sintering=""', "")
    s = s.replace('device\'="', "")
    s = s.replace('咪唑的方法\'="', "")
    s = s.replace('微波合成聚2,2"', "")
    s = s.replace('5,5\'', "")


    reg_id = r'<input type="hidden" name="vIdHidden" value="(.*)">'
    reg_time = r'<input type="hidden" name="nrdAdpHidden" value="(.*)">'
    # reg_holder = r'<input type="hidden" name="appNameHidden" value="&lt;FONT&gt;(.*)&lt;/FONT&gt;;">'
    reg_holder = r'<input type="hidden" name="appNameHidden" value="\s*(.*)\s*">'
    reg_name = r'<input type="hidden" name="titleHidden" value="(.*)">'
    reg_addre= r'<input type="hidden" name="appAddrHidden" value="\s*(.*)\s*>'


    timere_id = re.compile(reg_id)
    timere_time = re.compile(reg_time)
    timere_holder = re.compile(reg_holder)
    timere_name = re.compile(reg_name)
    timelist_addre = re.compile(reg_addre)

    timelist_id = re.findall(timere_id, s)
    timelist_time = re.findall(timere_time, s)
    timelist_holder = re.findall(timere_holder, s)
    timelist_name = re.findall(timere_name, s)
    timelist_addre = re.findall(timelist_addre, s)
    # print(len(timelist_id))

    for i in range(0, int(len(timelist_id))):
        print(str(timelist_id[i]) + "\t" + str(timelist_time[i]) + "\t" + str(timelist_holder[i]) + "\t\t" + str(timelist_name[i]) +"\t\t"+str(timelist_addre[i]))
        # 2数据库中插入数据
        #sql = "INSERT INTO neu (patent_id,year,patent_name,patent_holder,address) VALUES (%s,%s,%s,%s,%s)"
        #sql_insert1 = "INSERT INTO neu (patent_id,year,patent_name,patent_holder,address) VALUES ( '12803813', '2015.11.02',  '一种',  '东北大学', '沈阳');"
        sql_insert = "INSERT INTO neu (patent_id,year,patent_name,patent_holder,address) VALUES ( '"+str(timelist_id[i])+" ', '"+str(timelist_time[i])+" ',  ' "+str(timelist_name[i])+" ',  ' "+str(timelist_holder[i])+"', '"+str(timelist_addre[i])+" ');"
        # 执行语句
        #cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        #sql = "truncate table neu;"
       # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
       # print(cursor.rowcount)
# -*- coding: utf-8 -*-
from lxml import etree
#from scrapy.selector import Selector
import codecs
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
#print(conn)
#print(cursor)

#读取文件
#html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
#处理1-10页数据
print("*********")
print("开始处理数据")
try:
    for j in range(1, 1138):
        print("------------------")
        print("正在处理第%d页数据"%j)
        html = codecs.open("/Users/kun/Desktop/Patent_dut/patent" + str(j) + ".html", "r", "utf-8")

        content = html.read()
        html.close()
        #页面解析
        page_source = etree.HTML(content)
        #第一条专利信息
        #xpatn语句
        title_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[2]/div/p[5]/span/a/text()")
        id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[2]/div/p[1]/text()")
        holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[2]/div/p[6]/span/a/text()")
        date_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[2]/div/p[2]/a/text()")
        group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[1]/div/a[2]/text()")
        #处理专利名称信息
        for i in range(len(title_1)):
            #title_1[i] = title_1[i].replace(' ', '')
            title_1[i] = title_1[i].replace("'", "")
            title_1[i] = title_1[i].replace(")", "")
            title_1[i] = title_1[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_1)):
            group_1[i] = group_1[i].replace(' ', '')
            group_1[i] = group_1[i].replace('\r', '')
            group_1[i] = group_1[i].replace('\n', '')
            group_1[i] = group_1[i].replace('\t', '')
        for i in range(len(group_1)):
            group_1[i] = group_1[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_1)):
            holder_1[0] = '大连理工大学'
            holder_1[i] = holder_1[i].replace(' ', '')
            holder_1[i] = holder_1[i].replace('\r', '')
            holder_1[i] = holder_1[i].replace('\n', '')
            holder_1[i] = holder_1[i].replace('\t', '')
        for i in holder_1:
            if '' in holder_1:
                holder_1.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_1)):
            ipc_1[i] = ipc_1[i].replace(' ', '')
            ipc_1[i] = ipc_1[i].replace('\r', '')
            ipc_1[i] = ipc_1[i].replace('\n', '')
            ipc_1[i] = ipc_1[i].replace('\t', '')
        #打印信息
        #print(id_1)
        #print(date_1)
        #print(title_1)
        #print(ipc_1)
        #print(holder_1)
        #print(group_1)

        #合并ipc_1信息
        ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_1_one = list()
        ipc_1_one.append(ipc_1_joint)
        #合并专权人信息
        holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_1_one = list()
        holder_1_one.append(holder_1_joint)
        # 合并title信息
        title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_1_one = list()
        title_1_one.append(title_1_joint)
        #打印合并信息
        #print("*" * 10)
        #print("*" * 180)
        #print("   第" + str(j) + "页   " )
        #print("*" * 10)
        c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
            c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
            c_1[4]) + "','" + str(c_1[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)

        #print(c_1)
        #print("1" + '-' * 180)



        #####################################################################################
        #第2条专利信息
        #xpatn语句
        #title_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[1]/h1/div[2]/a/b/text()")
        title_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[2]/div/div[1]/h1/div[2]/a/b/text()")
        #ipc_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[1]/div/div[2]/div/p[5]/span/a/text()")
        ipc_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[2]/div/div[2]/div/p[5]/span/a/text()")
        id_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[2]/div/div[2]/div/p[1]/text()")
        holder_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[2]/div/div[2]/div/p[6]/span/a/text()")
        date_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[2]/div/div[2]/div/p[2]/a/text()")
        group_2 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[2]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_2)):
            #title_2[i] = title_2[i].replace(' ', '')
            title_2[i] = title_2[i].replace("'", "")
            title_2[i] = title_2[i].replace(")", "")
            title_2[i] = title_2[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_2)):
            group_2[i] = group_2[i].replace(' ', '')
            group_2[i] = group_2[i].replace('\r', '')
            group_2[i] = group_2[i].replace('\n', '')
            group_2[i] = group_2[i].replace('\t', '')
        for i in range(len(group_2)):
            group_2[i] = group_2[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_2)):
            holder_2[0] = '大连理工大学'
            holder_2[i] = holder_2[i].replace(' ', '')
            holder_2[i] = holder_2[i].replace('\r', '')
            holder_2[i] = holder_2[i].replace('\n', '')
            holder_2[i] = holder_2[i].replace('\t', '')
        for i in holder_2:
            if '' in holder_2:
                holder_2.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_2)):
            ipc_2[i] = ipc_2[i].replace(' ', '')
            ipc_2[i] = ipc_2[i].replace('\r', '')
            ipc_2[i] = ipc_2[i].replace('\n', '')
            ipc_2[i] = ipc_2[i].replace('\t', '')
        #打印信息
        #print(id_2)
        #print(date_2)
        #print(title_2)
        #print(ipc_2)
        #print(holder_2)
        #print(group_2)

        #合并ipc_1信息
        ipc_2_joint = ','.join(map(str, ipc_2))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_2_one = list()
        ipc_2_one.append(ipc_2_joint)
        #合并专权人信息
        holder_2_joint = ','.join(map(str, holder_2))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_2_one = list()
        holder_2_one.append(holder_2_joint)
        # 合并title信息
        title_2_joint = ''.join(map(str, title_2))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_2_one = list()
        title_2_one.append(title_2_joint)
        #打印合并信息
        #print('-' * 180)
        c_2 = id_2 + date_2 + title_2_one + holder_2_one + ipc_2_one + group_2
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
            c_2[0]) + "','" + str(c_2[1]) + "','" + str(c_2[2]) + "','" + str(c_2[3]) + "','" + str(
            c_2[4]) + "','" + str(c_2[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c2)
        #print("2" + '-' * 180)
        #################
        #第3条专利信息
        #xpatn语句
        title_3 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[3]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_3 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[3]/div/div[2]/div/p[5]/span/a/text()")
        id_3 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[3]/div/div[2]/div/p[1]/text()")
        holder_3 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[3]/div/div[2]/div/p[6]/span/a/text()")
        date_3 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[3]/div/div[2]/div/p[2]/a/text()")
        group_3 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[3]/div/div[1]/div/a[2]/text()")

        # 处理专利名称信息
        for i in range(len(title_3)):
            #title_3[i] = title_3[i].replace(' ', '')
            title_3[i] = title_3[i].replace("'", "")
            title_3[i] = title_3[i].replace(")", "")
            title_3[i] = title_3[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_3)):
            group_3[i] = group_3[i].replace(' ', '')
            group_3[i] = group_3[i].replace('\r', '')
            group_3[i] = group_3[i].replace('\n', '')
            group_3[i] = group_3[i].replace('\t', '')
        for i in range(len(group_3)):
            group_3[i] = group_3[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_3)):
            holder_3[0] = '大连理工大学'
            holder_3[i] = holder_3[i].replace(' ', '')
            holder_3[i] = holder_3[i].replace('\r', '')
            holder_3[i] = holder_3[i].replace('\n', '')
            holder_3[i] = holder_3[i].replace('\t', '')
        for i in holder_3:
            if '' in holder_3:
                holder_3.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_3)):
            ipc_3[i] = ipc_3[i].replace(' ', '')
            ipc_3[i] = ipc_3[i].replace('\r', '')
            ipc_3[i] = ipc_3[i].replace('\n', '')
            ipc_3[i] = ipc_3[i].replace('\t', '')
        #打印信息
        #print(id_3)
        #print(date_3)
        #print(title_3)
        #print(ipc_3)
        #print(holder_3)
        #print(group_3)

        #合并ipc_1信息
        ipc_3_joint = ','.join(map(str, ipc_3))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_3_one = list()
        ipc_3_one.append(ipc_3_joint)
        #合并专权人信息
        holder_3_joint = ','.join(map(str, holder_3))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_3_one = list()
        holder_3_one.append(holder_3_joint)
        # 合并title信息
        title_3_joint = ''.join(map(str, title_3))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_3_one = list()
        title_3_one.append(title_3_joint)
        #打印合并信息
        #print('-' * 180)
        c_3 = id_3 + date_3 + title_3_one + holder_3_one + ipc_3_one + group_3
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_3[0]) + "','" + str(c_3[1]) + "','" + str(c_3[2]) + "','" + str(c_3[3]) + "','" + str(
            c_3[4]) + "','" + str(c_3[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_3)
        #print("3" + '-' * 180)
        #######################
        #4
        #xpatn语句
        title_4 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[4]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_4 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[4]/div/div[2]/div/p[5]/span/a/text()")
        id_4 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[4]/div/div[2]/div/p[1]/text()")
        holder_4 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[4]/div/div[2]/div/p[6]/span/a/text()")
        date_4 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[4]/div/div[2]/div/p[2]/a/text()")
        group_4 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[4]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_4)):
            #title_4[i] = title_4[i].replace(' ', '')
            title_4[i] = title_4[i].replace("'", "")
            title_4[i] = title_4[i].replace(")", "")
            title_4[i] = title_4[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_4)):
            group_4[i] = group_4[i].replace(' ', '')
            group_4[i] = group_4[i].replace('\r', '')
            group_4[i] = group_4[i].replace('\n', '')
            group_4[i] = group_4[i].replace('\t', '')
        for i in range(len(group_4)):
            group_4[i] = group_4[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_4)):
            holder_4[0] = '大连理工大学'
            holder_4[i] = holder_4[i].replace(' ', '')
            holder_4[i] = holder_4[i].replace('\r', '')
            holder_4[i] = holder_4[i].replace('\n', '')
            holder_4[i] = holder_4[i].replace('\t', '')
        for i in holder_4:
            if '' in holder_4:
                holder_4.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_4)):
            ipc_4[i] = ipc_4[i].replace(' ', '')
            ipc_4[i] = ipc_4[i].replace('\r', '')
            ipc_4[i] = ipc_4[i].replace('\n', '')
            ipc_4[i] = ipc_4[i].replace('\t', '')
        #打印信息
        #print(id_4)
        #print(date_3)
        #print(title_4)
        #print(ipc_4)
        #print(holder_4)
        #print(group_4)

        #合并ipc_1信息
        ipc_4_joint = ','.join(map(str, ipc_4))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_4_one = list()
        ipc_4_one.append(ipc_4_joint)
        #合并专权人信息
        holder_4_joint = ','.join(map(str, holder_4))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_4_one = list()
        holder_4_one.append(holder_4_joint)
        # 合并title信息
        title_4_joint = ''.join(map(str, title_4))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_4_one = list()
        title_4_one.append(title_4_joint)
        #打印合并信息
        #print('-' * 180)
        c_4 = id_4 + date_4 + title_4_one + holder_4_one + ipc_4_one + group_4
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_4[0]) + "','" + str(c_4[1]) + "','" + str(c_4[2]) + "','" + str(c_4[3]) + "','" + str(
            c_4[4]) + "','" + str(c_4[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c4)
        #print("4" + '-' * 180)
        ######################
        #5
        #xpatn语句
        title_5 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[5]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_5 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[5]/div/div[2]/div/p[5]/span/a/text()")
        id_5 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[5]/div/div[2]/div/p[1]/text()")
        holder_5 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[5]/div/div[2]/div/p[6]/span/a/text()")
        date_5 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[5]/div/div[2]/div/p[2]/a/text()")
        group_5 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[5]/div/div[1]/div/a[2]/text()")
        #print(title_5)
        # 处理专利名称信息
        for i in range(len(title_5)):
            #title_5[i] = title_5[i].replace(',', '')
            title_5[i] = title_5[i].replace("'", "")
            title_5[i] = title_5[i].replace(")", "")
            title_5[i] = title_5[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_5)):
            group_5[i] = group_5[i].replace(' ', '')
            group_5[i] = group_5[i].replace('\r', '')
            group_5[i] = group_5[i].replace('\n', '')
            group_5[i] = group_5[i].replace('\t', '')
        for i in range(len(group_5)):
            group_5[i] = group_5[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_5)):
            holder_5[0] = '大连理工大学'
            holder_5[i] = holder_5[i].replace(' ', '')
            holder_5[i] = holder_5[i].replace('\r', '')
            holder_5[i] = holder_5[i].replace('\n', '')
            holder_5[i] = holder_5[i].replace('\t', '')
        for i in holder_5:
            if '' in holder_5:
                holder_5.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_5)):
            ipc_5[i] = ipc_5[i].replace(' ', '')
            ipc_5[i] = ipc_5[i].replace('\r', '')
            ipc_5[i] = ipc_5[i].replace('\n', '')
            ipc_5[i] = ipc_5[i].replace('\t', '')
        #打印信息
        #print(id_5)
        #print(date_5)
        #print(title_5)
        #print(ipc_5)
        #print(holder_5)
        #print(group_5)

        #合并ipc_1信息
        ipc_5_joint = ','.join(map(str, ipc_5))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_5_one = list()
        ipc_5_one.append(ipc_5_joint)
        # 合并title信息
        title_5_joint = ''.join(map(str, title_5))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_5_one = list()
        title_5_one.append(title_5_joint)
        #合并专权人信息
        holder_5_joint = ','.join(map(str, holder_5))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_5_one = list()
        holder_5_one.append(holder_5_joint)
        #打印合并信息
        #print('-' * 180)
        c_5 = id_5 + date_5 + title_5_one + holder_5_one + ipc_5_one + group_5
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_5[0]) + "','" + str(c_5[1]) + "','" + str(c_5[2]) + "','" + str(c_5[3]) + "','" + str(
            c_5[4]) + "','" + str(c_5[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c5)
        #print("5" + '-' * 180)
        #########
        #6
        #xpatn语句
        title_6 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[6]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_6 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[6]/div/div[2]/div/p[5]/span/a/text()")
        id_6 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[6]/div/div[2]/div/p[1]/text()")
        holder_6 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[6]/div/div[2]/div/p[6]/span/a/text()")
        date_6 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[6]/div/div[2]/div/p[2]/a/text()")
        group_6 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[6]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_6)):
            #title_6[i] = title_6[i].replace(',', '')
            title_6[i] = title_6[i].replace("'", "")
            title_6[i] = title_6[i].replace(")", "")
            title_6[i] = title_6[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_6)):
            group_6[i] = group_6[i].replace(' ', '')
            group_6[i] = group_6[i].replace('\r', '')
            group_6[i] = group_6[i].replace('\n', '')
            group_6[i] = group_6[i].replace('\t', '')
        for i in range(len(group_6)):
            group_6[i] = group_6[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_6)):
            holder_6[0] = '大连理工大学'
            holder_6[i] = holder_6[i].replace(' ', '')
            holder_6[i] = holder_6[i].replace('\r', '')
            holder_6[i] = holder_6[i].replace('\n', '')
            holder_6[i] = holder_6[i].replace('\t', '')
        for i in holder_6:
            if '' in holder_6:
                holder_6.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_6)):
            ipc_6[i] = ipc_6[i].replace(' ', '')
            ipc_6[i] = ipc_6[i].replace('\r', '')
            ipc_6[i] = ipc_6[i].replace('\n', '')
            ipc_6[i] = ipc_6[i].replace('\t', '')
        #打印信息
        #print(id_6)
        #print(date_6)
        #print(title_6)
        #print(ipc_6)
        #print(holder_6)
        #print(group_6)

        #合并ipc_1信息
        ipc_6_joint = ','.join(map(str, ipc_6))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_6_one = list()
        ipc_6_one.append(ipc_6_joint)
        #合并专权人信息
        holder_6_joint = ','.join(map(str, holder_6))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_6_one = list()
        holder_6_one.append(holder_6_joint)
        # 合并title信息
        title_6_joint = ''.join(map(str, title_6))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_6_one = list()
        title_6_one.append(title_6_joint)
        #打印合并信息
        #print('-' * 180)
        c_6 = id_6 + date_6 + title_6_one + holder_6_one + ipc_6_one + group_6
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_6[0]) + "','" + str(c_6[1]) + "','" + str(c_6[2]) + "','" + str(c_6[3]) + "','" + str(
            c_6[4]) + "','" + str(c_6[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_6)
        #print("6" + '-' * 180)
        #############
        #7
        #xpatn语句
        title_7 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[7]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_7 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[7]/div/div[2]/div/p[5]/span/a/text()")
        id_7 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[7]/div/div[2]/div/p[1]/text()")
        holder_7 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[7]/div/div[2]/div/p[6]/span/a/text()")
        date_7 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[7]/div/div[2]/div/p[2]/a/text()")
        group_7 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[7]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_7)):
            #title_7[i] = title_7[i].replace(' ', '')
            title_7[i] = title_7[i].replace("'", "")
            title_7[i] = title_7[i].replace(")", "")
            title_7[i] = title_7[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_7)):
            group_7[i] = group_7[i].replace(' ', '')
            group_7[i] = group_7[i].replace('\r', '')
            group_7[i] = group_7[i].replace('\n', '')
            group_7[i] = group_7[i].replace('\t', '')
        for i in range(len(group_7)):
            group_7[i] = group_7[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_7)):
            holder_7[0] = '大连理工大学'
            holder_7[i] = holder_7[i].replace(' ', '')
            holder_7[i] = holder_7[i].replace('\r', '')
            holder_7[i] = holder_7[i].replace('\n', '')
            holder_7[i] = holder_7[i].replace('\t', '')
        for i in holder_7:
            if '' in holder_7:
                holder_7.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_7)):
            ipc_7[i] = ipc_7[i].replace(' ', '')
            ipc_7[i] = ipc_7[i].replace('\r', '')
            ipc_7[i] = ipc_7[i].replace('\n', '')
            ipc_7[i] = ipc_7[i].replace('\t', '')
        #打印信息
        #print(id_7)
        #print(date_7)
        #print(title_7)
        #print(ipc_7)
        #print(holder_7)
        #print(group_7)

        #合并ipc_1信息
        ipc_7_joint = ','.join(map(str, ipc_7))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_7_one = list()
        ipc_7_one.append(ipc_7_joint)
        #合并专权人信息
        holder_7_joint = ','.join(map(str, holder_7))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_7_one = list()
        holder_7_one.append(holder_7_joint)
        # 合并title信息
        title_7_joint = ''.join(map(str, title_7))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_7_one = list()
        title_7_one.append(title_7_joint)
        #打印合并信息
        #print('-' * 180)
        c_7 = id_7 + date_7 + title_7_one + holder_7_one + ipc_7_one + group_7
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_7[0]) + "','" + str(c_7[1]) + "','" + str(c_7[2]) + "','" + str(c_7[3]) + "','" + str(
            c_7[4]) + "','" + str(c_7[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_7)
        #print("7" + '-' * 180)
        ##############
        #8
        #xpatn语句
        title_8 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[8]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_8 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[8]/div/div[2]/div/p[5]/span/a/text()")
        id_8 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[8]/div/div[2]/div/p[1]/text()")
        holder_8 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[8]/div/div[2]/div/p[6]/span/a/text()")
        date_8 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[8]/div/div[2]/div/p[2]/a/text()")
        group_8 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[8]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_8)):
            #title_8[i] = title_8[i].replace(' ', '')
            title_8[i] = title_8[i].replace("'", "")
            title_8[i] = title_8[i].replace(")", "")
            title_8[i] = title_8[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_8)):
            group_8[i] = group_8[i].replace(' ', '')
            group_8[i] = group_8[i].replace('\r', '')
            group_8[i] = group_8[i].replace('\n', '')
            group_8[i] = group_8[i].replace('\t', '')
        for i in range(len(group_8)):
            group_8[i] = group_8[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_8)):
            holder_8[0] = '大连理工大学'
            holder_8[i] = holder_8[i].replace(' ', '')
            holder_8[i] = holder_8[i].replace('\r', '')
            holder_8[i] = holder_8[i].replace('\n', '')
            holder_8[i] = holder_8[i].replace('\t', '')
        for i in holder_8:
            if '' in holder_8:
                holder_8.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_8)):
            ipc_8[i] = ipc_8[i].replace(' ', '')
            ipc_8[i] = ipc_8[i].replace('\r', '')
            ipc_8[i] = ipc_8[i].replace('\n', '')
            ipc_8[i] = ipc_8[i].replace('\t', '')
        #打印信息
        #print(id_8)
        #print(date_8)
        #print(title_8)
        #print(ipc_8)
        #print(holder_8)
        #print(group_8)

        #合并ipc_1信息
        ipc_8_joint = ','.join(map(str, ipc_8))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_8_one = list()
        ipc_8_one.append(ipc_8_joint)
        #合并专权人信息
        holder_8_joint = ','.join(map(str, holder_8))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_8_one = list()
        holder_8_one.append(holder_8_joint)
        # 合并title信息
        title_8_joint = ''.join(map(str, title_8))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_8_one = list()
        title_8_one.append(title_8_joint)
        #打印合并信息
        #print('-' * 180)
        c_8 = id_8 + date_8 + title_8_one + holder_8_one + ipc_8_one + group_8
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_8[0]) + "','" + str(c_8[1]) + "','" + str(c_8[2]) + "','" + str(c_8[3]) + "','" + str(
            c_8[4]) + "','" + str(c_8[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_8)
        #print("8" + '-' * 180)
        #####################
        #9
        #xpatn语句
        title_9 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[9]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_9 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[9]/div/div[2]/div/p[5]/span/a/text()")
        id_9 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[9]/div/div[2]/div/p[1]/text()")
        holder_9 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[9]/div/div[2]/div/p[6]/span/a/text()")
        date_9 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[9]/div/div[2]/div/p[2]/a/text()")
        group_9 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[9]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_9)):
            #title_9[i] = title_9[i].replace(' ', '')
            title_9[i] = title_9[i].replace("'", "")
            title_9[i] = title_9[i].replace(")", "")
            title_9[i] = title_9[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_9)):
            group_9[i] = group_9[i].replace(' ', '')
            group_9[i] = group_9[i].replace('\r', '')
            group_9[i] = group_9[i].replace('\n', '')
            group_9[i] = group_9[i].replace('\t', '')
        for i in range(len(group_9)):
            group_9[i] = group_9[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_9)):
            holder_9[0] = '大连理工大学'
            holder_9[i] = holder_9[i].replace(' ', '')
            holder_9[i] = holder_9[i].replace('\r', '')
            holder_9[i] = holder_9[i].replace('\n', '')
            holder_9[i] = holder_9[i].replace('\t', '')
        for i in holder_9:
            if '' in holder_9:
                holder_9.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_9)):
            ipc_9[i] = ipc_9[i].replace(' ', '')
            ipc_9[i] = ipc_9[i].replace('\r', '')
            ipc_9[i] = ipc_9[i].replace('\n', '')
            ipc_9[i] = ipc_9[i].replace('\t', '')
        #打印信息
        #print(id_9)
        #print(date_9)
        #print(title_9)
        #print(ipc_9)
        #print(holder_9)
        #print(group_9)

        #合并ipc_1信息
        ipc_9_joint = ','.join(map(str, ipc_9))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_9_one = list()
        ipc_9_one.append(ipc_9_joint)
        # 合并title信息
        title_9_joint = ''.join(map(str, title_9))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_9_one = list()
        title_9_one.append(title_9_joint)
        #合并专权人信息
        holder_9_joint = ','.join(map(str, holder_9))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_9_one = list()
        holder_9_one.append(holder_9_joint)
        #打印合并信息
        #print('-' * 180)
        c_9 = id_9 + date_9 + title_9_one + holder_9_one + ipc_9_one + group_9
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_9[0]) + "','" + str(c_9[1]) + "','" + str(c_9[2]) + "','" + str(c_9[3]) + "','" + str(
            c_9[4]) + "','" + str(c_9[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_9)
        #print("9" + '-' * 180)
        #################
        #10
        #xpatn语句
        title_10 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[10]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_10 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[10]/div/div[2]/div/p[5]/span/a/text()")
        id_10 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[10]/div/div[2]/div/p[1]/text()")
        holder_10 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[10]/div/div[2]/div/p[6]/span/a/text()")
        date_10 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[10]/div/div[2]/div/p[2]/a/text()")
        group_10 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[10]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_10)):
            #title_10[i] = title_10[i].replace(' ', '')
            title_10[i] = title_10[i].replace("'", "")
            title_10[i] = title_10[i].replace(")", "")
            title_10[i] = title_10[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_10)):
            group_10[i] = group_10[i].replace(' ', '')
            group_10[i] = group_10[i].replace('\r', '')
            group_10[i] = group_10[i].replace('\n', '')
            group_10[i] = group_10[i].replace('\t', '')
        for i in range(len(group_10)):
            group_10[i] = group_10[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_10)):
            holder_10[0] = '大连理工大学'
            holder_10[i] = holder_10[i].replace(' ', '')
            holder_10[i] = holder_10[i].replace('\r', '')
            holder_10[i] = holder_10[i].replace('\n', '')
            holder_10[i] = holder_10[i].replace('\t', '')
        for i in holder_10:
            if '' in holder_10:
                holder_10.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_10)):
            ipc_10[i] = ipc_10[i].replace(' ', '')
            ipc_10[i] = ipc_10[i].replace('\r', '')
            ipc_10[i] = ipc_10[i].replace('\n', '')
            ipc_10[i] = ipc_10[i].replace('\t', '')
        #打印信息
        #print(id_10)
        #print(date_10)
        #print(title_10)
        #print(ipc_10)
        #print(holder_10)
        #print(group_10)

        #合并ipc_1信息
        ipc_10_joint = ','.join(map(str, ipc_10))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_10_one = list()
        ipc_10_one.append(ipc_10_joint)
        #合并专权人信息
        holder_10_joint = ','.join(map(str, holder_10))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_10_one = list()
        holder_10_one.append(holder_10_joint)
        # 合并title信息
        title_10_joint = ''.join(map(str, title_10))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_10_one = list()
        title_10_one.append(title_10_joint)
        #打印合并信息
        #print('-' * 180)
        c_10 = id_10 + date_10 + title_10_one + holder_10_one + ipc_10_one + group_10
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_10[0]) + "','" + str(c_10[1]) + "','" + str(c_10[2]) + "','" + str(c_10[3]) + "','" + str(
            c_10[4]) + "','" + str(c_10[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_10)
        #print("10" + '-' * 180)
        #############
        #11
        #xpatn语句
        title_11 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[11]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_11 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[11]/div/div[2]/div/p[5]/span/a/text()")
        id_11 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[11]/div/div[2]/div/p[1]/text()")
        holder_11 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[11]/div/div[2]/div/p[6]/span/a/text()")
        date_11 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[11]/div/div[2]/div/p[2]/a/text()")
        group_11 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[11]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_11)):
            #title_11[i] = title_11[i].replace(' ', '')
            title_11[i] = title_11[i].replace("'", "")
            title_11[i] = title_11[i].replace(")", "")
            title_11[i] = title_11[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_11)):
            group_11[i] = group_11[i].replace(' ', '')
            group_11[i] = group_11[i].replace('\r', '')
            group_11[i] = group_11[i].replace('\n', '')
            group_11[i] = group_11[i].replace('\t', '')
        for i in range(len(group_11)):
            group_11[i] = group_11[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_11)):
            holder_11[0] = '大连理工大学'
            holder_11[i] = holder_11[i].replace(' ', '')
            holder_11[i] = holder_11[i].replace('\r', '')
            holder_11[i] = holder_11[i].replace('\n', '')
            holder_11[i] = holder_11[i].replace('\t', '')
        for i in holder_11:
            if '' in holder_11:
                holder_11.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_11)):
            ipc_11[i] = ipc_11[i].replace(' ', '')
            ipc_11[i] = ipc_11[i].replace('\r', '')
            ipc_11[i] = ipc_11[i].replace('\n', '')
            ipc_11[i] = ipc_11[i].replace('\t', '')
        #打印信息
        #print(id_11)
        #print(date_11)
        #print(title_11)
        #print(ipc_11)
        #print(holder_11)
        #print(group_11)

        #合并ipc_1信息
        ipc_11_joint = ','.join(map(str, ipc_11))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_11_one = list()
        ipc_11_one.append(ipc_11_joint)
        #合并专权人信息
        holder_11_joint = ','.join(map(str, holder_11))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_11_one = list()
        holder_11_one.append(holder_11_joint)
        # 合并title信息
        title_11_joint = ''.join(map(str, title_11))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_11_one = list()
        title_11_one.append(title_11_joint)
        #打印合并信息
        #print('-' * 180)
        c_11 = id_11 + date_11 + title_11_one + holder_11_one + ipc_11_one + group_11
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_11[0]) + "','" + str(c_11[1]) + "','" + str(c_11[2]) + "','" + str(c_11[3]) + "','" + str(
            c_11[4]) + "','" + str(c_11[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_11)
        #print("11" + '-' * 180)
        ###########
        #12
        #xpatn语句
        title_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[1]/h1/div[2]/a/b/text()")
        ipc_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[5]/span/a/text()")
        id_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[1]/text()")
        holder_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[6]/span/a/text()")
        date_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[2]/a/text()")
        group_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[1]/div/a[2]/text()")
        # 处理专利名称信息
        for i in range(len(title_12)):
            #title_12[i] = title_12[i].replace(' ', '')
            title_12[i] = title_12[i].replace("'", "")
            title_12[i] = title_12[i].replace(")", "")
            title_12[i] = title_12[i].replace('(', '')
        #处理同族信息
        for i in range(len(group_12)):
            group_12[i] = group_12[i].replace(' ', '')
            group_12[i] = group_12[i].replace('\r', '')
            group_12[i] = group_12[i].replace('\n', '')
            group_12[i] = group_12[i].replace('\t', '')
        for i in range(len(group_12)):
            group_12[i] = group_12[i].replace('同族：', '')
        #处理专权人信息
        for i in range(len(holder_12)):
            holder_12[0] = '大连理工大学'
            holder_12[i] = holder_12[i].replace(' ', '')
            holder_12[i] = holder_12[i].replace('\r', '')
            holder_12[i] = holder_12[i].replace('\n', '')
            holder_12[i] = holder_12[i].replace('\t', '')
        for i in holder_12:
            if '' in holder_12:
                holder_12.remove('')
        #处理ipc_1分类号信息
        for i in range(len(ipc_12)):
            ipc_12[i] = ipc_12[i].replace(' ', '')
            ipc_12[i] = ipc_12[i].replace('\r', '')
            ipc_12[i] = ipc_12[i].replace('\n', '')
            ipc_12[i] = ipc_12[i].replace('\t', '')
        #打印信息
        #print(id_12)
        #print(date_12)
        #print(title_12)
        #print(ipc_12)
        #print(holder_12)
        #print(group_12)

        #合并ipc_1信息
        ipc_12_joint = ','.join(map(str, ipc_12))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        ipc_12_one = list()
        ipc_12_one.append(ipc_12_joint)
        #合并专权人信息
        holder_12_joint = ','.join(map(str, holder_12))  # join 操作不是 str类型的列表会报错，得先转换哈
        holder_12_one = list()
        holder_12_one.append(holder_12_joint)
        # 合并title信息
        title_12_joint = ''.join(map(str, title_12))  # join 操作不是 str类型的列表会报错，得先转换哈
        # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
        title_12_one = list()
        title_12_one.append(title_12_joint)
        #打印合并信息
        #print('-' * 180)
        c_12 = id_12 + date_12 + title_12_one + holder_12_one + ipc_12_one + group_12
        sql_insert = "INSERT INTO dut_info (p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ('" + str(
            c_12[0]) + "','" + str(c_12[1]) + "','" + str(c_12[2]) + "','" + str(c_12[3]) + "','" + str(
            c_12[4]) + "','" + str(c_12[5]) + "');"
        # 执行语句
        # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
        cursor.execute(sql_insert)
        # sql = "truncate table neu;"
        # cursor.execute(sql)
        # 事务提交，否则数据库得不到更新
        conn.commit()
        # print(cursor.rowcount)
        #print(c_12)
        #print("12"+'-' * 180)
        #if (j == 10):
        #    print("*" * 180)
    print("-----------------")
    print("数据处理完成！")
except:
    print("*****************")
finally:
    print("数据处理完成！")



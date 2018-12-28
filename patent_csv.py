# coding=utf-8
import pymysql
import csv
# 建立数据库连接
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
# print(cursor)

# 1、从数据库中查询
# sql="INSERT INTO login(user_name,pass_word)"
#sql = "select patent_holder as '联合申请人',count(patent_holder) as '申请数量'  from neu where patent_holder not like '%东北大学;' group by patent_holder"
sql = "select patent_holder as '联合申请人',count(patent_holder) as '申请数量'  from neu where patent_holder not like '%东北大学;' group by patent_holder order by count(patent_holder) desc;"
# cursor执行sql语句
cursor.execute(sql)
# 打印执行结果的条数
#print(cursor.rowcount)

# 使用fetch方法进行遍历结果  总共有三条数据

# rs=cursor.fetchone()#将第一条结果放入rs中
# re=cursor.fetchmany(3)#将多个结果放入re中
rr = cursor.fetchall()  # 将所有的结果放入rr中
# 对结果进行处理
#print("编号  级别  工资")
"""f = open('patent.txt', 'a')
#print(rr)
for row in rr:
    #print(row[0],row[1])
    patent = row[0]
    num = row[1]
    #print(type(patent))
    #print(type(num))
    f.write("东北大学\t")
    f.write(patent.replace("东北大学;","").replace(";",",")[:-1])
    f.write('\t'+str(num))
    f.write("\n")

f.close()
"""
# 从列表写入csv文件
csvFile2 = open('patent.csv','w',encoding='gb18030') # 设置newline，否则两行之间会空一行
writer = csv.writer(csvFile2)
patent_list = []
for row in rr:
    patent = row[0]
    num = row[1]
    row1 = "东北大学"
    row2 = patent.replace("东北大学;","").replace(";",",")[:-1]
    row3 = str(row[1])

    writer.writerow([row1,row2,row3])
    #patent_list = row.append(row1)
    #patent_list = row.append(row2)
    #patent_list = row.append(row3)
#print(patent_list)
#print(rr)
#writer.writerow(patent_list)
#writer.writerow(rr)
csvFile2.close()

"""
def __init__(self):
    self.csv_file = csv.writer(
        open('ajk_sh_sp_{0}.csv'.format(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")), 'w',
             encoding='gb18030'))
    # self.csv_file = csv.writer(open('ajk_sh_sp_{0}.csv'.format(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")),'w',encoding='gb18030'))


def process_item(self, item, spider):
    self.csv_file.writerow(
        [item['title'], item['link'], item['address'], item['house_type'], item['info'], item['price'], item['phone']])
    return item
"""
#print(str(cursor.rowcount)+"条专利文献写入成功")
# print(re)#输出两条数据，因为fetch()方法是建立在上一次fetch()方法基础上的
# 数据库连接和游标的关闭
conn.close()
cursor.close()
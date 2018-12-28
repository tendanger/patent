#xpatn语句
title_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[1]/h1/div[2]/a/b/text()")
ipc_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[5]/span/a/text()")
id_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[1]/text()")
holder_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[6]/span/a/text()")
date_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[2]/div/p[2]/a/text()")
group_12 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li[12]/div/div[1]/div/a[2]/text()")
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
    holder_12[0] = '东北大学'
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
#打印合并信息
#print('-' * 180)
c_12 = id_12 + date_12 + title_12 + holder_12_one + ipc_12_one + group_12
print(c_12)
print('-' * 180)
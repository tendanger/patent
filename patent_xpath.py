# -*- coding: utf-8 -*-
from lxml import etree
from scrapy.selector import Selector
import codecs

html1 = """<p class="clear">
										        	
										        	
										        	
										        		<b class="in-bl" style="float:left;margin:5px 0;">IPC分类号 : </b>
										        		
											        		
											        			<span class="in-bl" style="margin:5px 0;float:left;max-width:300px;text-overflow: ellipsis;overflow: hidden;white-space: nowrap;">
											        			<a href="javascript:;" _name="G01N1/28" onclick="drillSearch('IVDB045','IPC分类号','','false',this);return false;">
											        				G01N1/28
											        			</a>;
											        			</span>
											        		
											        			<span class="in-bl" style="margin:5px 0;float:left;max-width:300px;text-overflow: ellipsis;overflow: hidden;white-space: nowrap;">
											        			<a href="javascript:;" _name="G01N1/32" onclick="drillSearch('IVDB045','IPC分类号','','false',this);return false;">
											        				G01N1/32
											        			</a>;
											        			</span>
											        		
											        	
										        	
											        </p>"""


# f = open("patent1.html", 'rb').read() #二进制方式打开，读入比特流
#f1 = open("/Users/kun/Desktop/patent_neu/patent_html/patent1.html", 'rb').read()
#s = f1.decode() #解码
html = codecs.open("/Users/kun/Desktop/patent_neu/patent_html/patent1.html","r","utf-8")

#html = html.replace("\n", "")
#html = html.replace("\t", "")
#html = html.replace(" ", "")
content=html.read()
#content = content.replace("\n", "")
#content = content.replace("\t", "")
#content = content.replace("\r", "")
html.close()
#tree=etree.HTML(content)


page_source = etree.HTML(content)

title = page_source.xpath("//*[@id='search_result']/div[4]/div[1]/ul/li[7]/div/div[1]/h1/div[2]/a/b/text()")
ipc = page_source.xpath("//*[@id='search_result']/div[4]/div[1]/ul/li[7]/div/div[2]/div/p[5]/span/a/text()")
id = page_source.xpath("//*[@id='search_result']/div[4]/div[1]/ul/li[1]/div/div[2]/div/p[1]/text()")
holder = page_source.xpath("//*[@id='search_result']/div[4]/div[1]/ul/li[7]/div/div[2]/div/p[6]/span/a/text()")
date = page_source.xpath("//*[@id='search_result']/div[4]/div[1]/ul/li[7]/div/div[2]/div/p[2]/a/text()")
group = page_source.xpath("//*[@id='search_result']/div[4]/div[1]/ul/li[7]/div/div[1]/div/a[2]/text()")

for i in range(len(group)):
    group[i] = group[i].replace(' ','')
    group[i] = group[i].replace('\r', '')
    group[i] = group[i].replace('\n', '')
    group[i] = group[i].replace('\t', '')


#print(ipc)
for i in range(len(holder)):
    holder[0] = '东北大学'
    holder[i] = holder[i].replace(' ','')
    holder[i] = holder[i].replace('\r', '')
    holder[i] = holder[i].replace('\n', '')
    holder[i] = holder[i].replace('\t', '')
for i in holder:
   if '' in holder:
        holder.remove('')


#ipc = page_source.xpath("//div/p/span/a")
#print(ipc.xpath('string(.)').strip())
for i in range(len(ipc)):
    ipc[i] = ipc[i].replace(' ','')
    ipc[i] = ipc[i].replace('\r', '')
    ipc[i] = ipc[i].replace('\n', '')
    ipc[i] = ipc[i].replace('\t', '')

for i in range (len(group)):
    group[i] = group[i].replace('同族：','')

#info = title[0].xpath('string(.)')
#info = title.xpath("string(.)").extract()
#title = title.xpath('string(.)')

#all_href = page_source.xpath("//a/@href")

#data = Selector(text=tree).xpath("//title/text()")

#data = page_source.xpath("//title/text()")
#info = data.xpath("string(.)").extract()
print(id)
print(date)
print(title)
print(ipc)
print(holder)
print(group)
#print(ipc)
#print(data)
#print(info)



ipc_joint = ','.join(map(str,ipc))#join 操作不是 str类型的列表会报错，得先转换哈
#ipc_joint = eval(str(ipc).replace(',','').replace(' ',''))
ipc_one = list()
#b = ipc_joint
ipc_one.append(ipc_joint)
#print(ipc_one)

holder_joint = ','.join(map(str,holder))#join 操作不是 str类型的列表会报错，得先转换哈
holder_one = list()
#b = holder_joint
holder_one.append(holder_joint)
#print(holder_one)


print('-'*180)
c = id + date + title + holder_one + ipc_one + group
print(c)
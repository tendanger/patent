# -*- coding: utf-8 -*-
import re

f1= open("/Users/kun/Desktop/patent_html/patent.html", 'rb').read() #二进制方式打开
#f1= open("/Users/kun/Desktop/patent_html/patent"+str(i)+".html", 'rb').read()
s= f1.decode()
#s = f.replace("&gt","")



reg_id = r'<input type="hidden" name="vIdHidden" value="(.*)">'
reg_time = r'<input type="hidden" name="nrdAdpHidden" value="(.*)">'
#reg_holder = r'<input type="hidden" name="appNameHidden" value="&lt;FONT&gt;(.*)&lt;/FONT&gt;;">'
reg_holder = r'<input type="hidden" name="appNameHidden" value="\s*(.*)\s*">'
reg_name = r'<input type="hidden" name="titleHidden" value="(.*)">'

timere_id = re.compile(reg_id)
timere_time = re.compile(reg_time)
timere_holder = re.compile(reg_holder)
timere_name = re.compile(reg_name)

timelist_id = re.findall(timere_id,s)
timelist_time = re.findall(timere_time,s)
timelist_holder = re.findall(timere_holder,s)
timelist_name = re.findall(timere_name,s)
#print(len(timelist_id))
j=0
for i in range(0,int(len(timelist_holder))):
    #print(str(timelist_id[i])+"\t"+str(timelist_time[i])+"\t"+str(timelist_holder[i])+"\t"+str(timelist_name[i]))
    print(str(timelist_holder[i]))
    j+=1
print(j)
    #+"\t"+str(timelist_time[i])+"\t"+str(timelist_holder[i])+"\t"+str(timelist_name[i]))
#print("第"+str(page)+"页专利信息列表，共："+str(i+1)+"条，与实际数据匹配！")
#print(timelist_holder[11])

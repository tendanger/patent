# -*- coding: utf-8 -*-
import re
for  i in range(1,754):
        #f = open("patent1.html", 'rb').read() #二进制方式打开
        f1= open("/Users/kun/Desktop/patent_html/patent"+str(i)+".html", 'rb').read()
        s = f1.decode()



        reg_id = r'<input\s*type="hidden"\s*name="vIdHidden"\s*value="(.*)">'
        reg_time = r'<input\s*type="hidden"\s*name="nrdAdpHidden"\s*value="(.*)">'
        #reg_holder = r'<input\s*type="hidden"\s*name="appNameHidden"\s*value=".*gt;(.*)&lt;/FONT&gt;;">'
        reg_holder= r'<input\s*type="hidden"\s*name="appNameHidden"\s*value="*(.*)">'
        reg_name = r'<input\s*type="hidden"\s*name="titleHidden"\s*value="(.*)">'


        try:
                timere_id = re.compile(reg_id)
                timere_time = re.compile(reg_time)
                timere_holder = re.compile(reg_holder)
                timere_name = re.compile(reg_name)

                timelist_id = re.findall(timere_id,s)
                timelist_time = re.findall(timere_time,s)
                timelist_holder = re.findall(timere_holder,s)
                timelist_name = re.findall(timere_name,s)
                #print(len(timelist_id))

                for i in range(0,int(len(timelist_id))):
                    print(str(timelist_id[i])+","+str(timelist_time[i])+","+str(timelist_holder[i])+","+str(timelist_name[i]))

                #print("第"+str(page)+"页专利信息列表，共："+str(i+1)+"条，与实际数据匹配！")
                #print(timelist_holder[11])
        except Exception as e:
            continue
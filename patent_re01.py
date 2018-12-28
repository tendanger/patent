# -*- coding: utf-8 -*-
import re

for i in range(1, 755):
    # f = open("patent1.html", 'rb').read() #二进制方式打开，读入比特流
    f1 = open("/Users/kun/Desktop/patent_html/patent" + str(i) + ".html", 'rb').read()
    s = f1.decode() #解码
    s = s.replace("&lt;FONT&gt;东北大学&lt", "东北大学")
    s = s.replace("/FONT&gt;", ";")
    s = s.replace("东北大学;;;", "东北大学;")
    s = s.replace("东北大学;,", "东北大学,")
    s = s.replace("东北大学;;", "东北大学,")
    s = s.replace("东北大学,", "东北大学;")
    s = s.replace("辽宁省沈阳市和平区文化路3号巷11号;\"", "辽宁省沈阳市和平区文化路3号巷11号")
    #s = s.replace("/FONT&gt", "")

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

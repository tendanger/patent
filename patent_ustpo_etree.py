import xml.etree.ElementTree as ET
import os
print(os.getcwd())
xmlFilePath = os.path.abspath("ustpo_etree.xml")
tree = ET.parse(xmlFilePath)

root = tree.getroot()

print(root.tag)
#print("------------------------------------")
# 遍历xml文档
for subchild in root:
    #print(subchild.tag, subchild.attrib)
    #print("****************")
    for sub2child in subchild:
        #print(sub2child.tag,sub2child.attrib)
        #print("###")

        #for sub3child in sub2child:
        for node in sub2child.findall('document-id'):
            country = node.find('country').text
            doc_number = node.find('doc-number').text
            date = node.find('date').text
            print(country,doc_number,date)

        for sub3child in sub2child:

            for node in sub3child.findall('addressbook'):
                orgname = node.find('orgname').text
                print(orgname)


            for sub4child in sub3child:

                for node in sub4child.findall('address'):
                    city = node.find('city').text
                    country = node.find('country').text
                    print(city, country)

                for node in sub4child.findall('addressbook'):
                    last_name = node.find('last-name').text
                    first_name = node.find('first-name').text
                    print(last_name,first_name)
                for sub5child in sub4child:
                    for node in sub5child.findall('address'):
                        city = node.find('city').text
                        print(city)
                        print('\n')

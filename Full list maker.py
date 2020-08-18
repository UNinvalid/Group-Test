import requests
import re
import persian
coding1 = "utf-8"
coding2 = "gb18030"
f=open("Name.txt", 'r', encoding=coding1)
txt=f.readlines()
for item in txt:
    item.replace('\n','')
    item.replace(' ','')
    Shenas="https://omid.algo.ir/api/core/search/" + item
    ID=requests.get(Shenas)
    search=ID.text.split('"')
    search[17]=search[17].replace("/search/",'')
    search[17]=search[17].replace("%20%20%20%0A", '')
    Shenas="https://omid.algo.ir/api/core/search/" + search[17]
    ID=requests.get(Shenas)
    search=ID.text
    regex=re.findall(r'(?<=GROUP)[^.\s]*', search)
    print("GROUP",regex[0][0:3],end='')
    search=ID.text.split('"')
    print (search[7])



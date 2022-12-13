import re
p=re.compile('\d{3}[-|\.|\s]\d{3}[-|\.|\s]\d{4}')
r=p.findall('3345-766-907 ,886-245-9772')
print(r)

a=re.compile('\w+\d+\w*@gmail\.com')
t=a.findall(' sumahsn2002@gmail.com,shhdh.in,sushma2008@gmail.com')
print(t)

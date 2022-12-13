import re
p=re.compile('\d{3}[-|\.|\s]\d{3}[-|\.|\s]\d{4}')
r=p.search('345-766-9087 is an American number')
print(r.group())

a=re.compile('\w+\d+\w*@gmail\.com')
t=a.search('mail id is sumahsn2002@gmail.com')
print(t.group())

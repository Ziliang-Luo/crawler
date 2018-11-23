#IP地址的正则表达式:
#((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))

import re


#search()
match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print('search=' + match.group(0))


#match()
match = re.search(r'[1-9]\d{5}','100081 BIT')
if match:
    print('match=' +match.group(0))

#findall()
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100085')
print ('findal:')
print (ls)

#split()
sp = re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
print ('split:')
print (sp)

#split(maxsplit)
sp = re.split(r'[1-9]\d{5}','BIT100081 TSU100084', maxsplit=1)
print ('maxsplit:')
print (sp)

#finditer
print('finditer:')
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100085'):
    if m:
        print (m.group(0))

#编译，多次使用
regex = re.compile(r'[1-9]\d{5}')
r = regex.search('BIT100081')

#sub
print('sub')
sub = re.sub(r'[1-9]\d{5}','zipcode','BIT100081 TSU100085')
print(sub)

import requests
from bs4 import BeautifulSoup
import re
url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
print (soup.prettify())
tag = soup.title.parent
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

#查找所有的a标签
for link in soup.find_all('a'):
    print (link.get('href'))

#find_all(True)打印所有标签
#find_all(name, attrs, recursive, string,**kwargs)
#查找以'b'开头的标签
for tag in soup.find_all(re.compile('b')):
    print (tag.name)

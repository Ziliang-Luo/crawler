#百度
#修改params
import requests
url = 'https://www.baidu.com/s'
kv = {'wd': 'Python'}
r = requests.get('https://www.baidu.com/s',params=kv)
r.raise_for_status()
r.encoding = r.apparent_encoding
print (r.status_code)
print (r.request.url)
print (r.text)
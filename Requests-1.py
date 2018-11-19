#爬取京东
#修改headers
import requests
try:
    url = 'https://www.amazon.cn/dp/B01M8L5Z3Y'
    kv = {'user-agent' : 'Mozilla/5.0'}
    r = requests.get(url,headers= kv)
    print (r.status_code)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.text[1000:2000])
except:
    print('爬取失败')

#查找ip地址归属地

import requests
url = 'http://m.ip138.com/ip.asp?ip='
try:
    r = requests.get(url+'50.81.231.170')
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.status_code)
    print(r.text[-500:])

except:
    print('爬取失败')
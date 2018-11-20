#抓取图片

import requests
import os
url = 'https://img4q.duitang.com/uploads/item/201306/11/20130611140903_UtnXB.thumb.700_0.jpeg'
root = '//Users//ziliangluo//Documents//2018fall//python//crawler//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')

except:
    print('爬取失败')


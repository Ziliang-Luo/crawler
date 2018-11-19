import time
import requests
#
def getHtml(url):
    try:
        a=requests.get(url)
        a.raise_for_status
        return a.text
    except:
        return ''
#
def main():
    url='http://www.baidu.com'
    #
    start_time=time.time()
    #
    for i in range(100):
        r=getHtml(url)
        if r!='':
            print('成功爬取第{}次'.format(i+1))
        else:
            print('爬取第{}次失败'.format(i+1))
    #
    end_time=time.time()
    #
    print('一共消耗时间: {} 秒.'.format(end_time - start_time))
#
main()

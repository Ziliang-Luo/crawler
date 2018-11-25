#淘宝商品比价

import requests
import re

def getHTMLText(url,cookies,kv):
    try:
        r = requests.get(url, cookie=cookies, headers = kv,timeout=30)
        r.raise_for_status()
        r.encoding =r.apparent_encoding
        return r.text
    except:
        return ''


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price =eval(plt[i].split(':')[1])
            title =eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print('')




def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print (tplt.format('序号','价格','名称'))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0], g[1]))



def main():
    goods = '书包'
    depth = 2
    cookies = {}
    coo = 't=54c076b4938c7d00c0b2dad5bee5859f; thw=us; cna=FrlXFAZbdFQCAYH/4UjcwIsZ; v=0; cookie2=129e8d16c6ea4b676782b02e36b08c22; _tb_token_=eae5eeee57663; _m_h5_tk=9d34e6378f7845bf3f5d5fba8f360845_1542585992630; _m_h5_tk_enc=0f51c12b86eaf4345d0f6b2b34f3835c; unb=2518574128; sg=188; _l_g_=Ug%3D%3D; skt=6ae77ae2625438d2; cookie1=BxBBhof2O3ZPFv9GYaRZqRFuFRFbyPloBK2dw14yo8Y%3D; csg=7b353908; uc3=vt3=F8dByR6tG%2FndW0XE%2BNo%3D&id2=UU2zWEY83QvJUw%3D%3D&nk2=Dl9OSuEBXckgvrMDjw%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU0MjU3ODg2MA%3D%3D; tracknick=moon382097831; lgc=moon382097831; _cc_=W5iHLLyFfA%3D%3D; dnk=moon382097831; _nk_=moon382097831; cookie17=UU2zWEY83QvJUw%3D%3D; tg=0; l=And3H9mmrrHwaCeAN5lYh38Ch2DBTkue; enc=7rn9j6xniPQPACsWuCyLaKo1KxGiXNDhDk%2F6LsbR6XMnyF%2BVERQgu%2F04hTQkasHHjLyvc9n%2BTIF8CCEM5RsRKg%3D%3D; mt=ci=0_1; uc1="cookie15=UtASsssmOIJ0bQ%3D%3D"; hng=US%7Czh-CN%7CUSD%7C840; isg=BO3tuVh7Sr3_uy7RfSDZE-Dk_I-n4iF7szwLPS_yKQTzpg1Y95ox7DtwlCLlJjnU'
    kv= {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    start_url = 'https://www.s.taobao.com/search?q=' + goods
    for line in coo.split(';'):
        name,value=line.strip().split('=',1)
        cookies[name]=value
    infoList =[]
    for i in range(depth):
        try:
            url = start_url + '&s' + str(44*i)
            html = getHTMLText(url,cookies,kv)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)

main()

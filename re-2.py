import requests
import re


def getHTMLText(url, kv, cookies):
    try:
        r = requests.get(url, cookies=cookies, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('')


def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format("序号", "价格", "商品标题"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?&q=' + goods
    coo = 't=54c076b4938c7d00c0b2dad5bee5859f; thw=us; cna=FrlXFAZbdFQCAYH/4UjcwIsZ; v=0; cookie2=129e8d16c6ea4b676782b02e36b08c22; _tb_token_=eae5eeee57663; _m_h5_tk=9d34e6378f7845bf3f5d5fba8f360845_1542585992630; _m_h5_tk_enc=0f51c12b86eaf4345d0f6b2b34f3835c; unb=2518574128; sg=188; _l_g_=Ug%3D%3D; cookie1=BxBBhof2O3ZPFv9GYaRZqRFuFRFbyPloBK2dw14yo8Y%3D; tracknick=moon382097831; lgc=moon382097831; dnk=moon382097831; _nk_=moon382097831; cookie17=UU2zWEY83QvJUw%3D%3D; tg=0; enc=7rn9j6xniPQPACsWuCyLaKo1KxGiXNDhDk%2F6LsbR6XMnyF%2BVERQgu%2F04hTQkasHHjLyvc9n%2BTIF8CCEM5RsRKg%3D%3D; hng=US%7Czh-CN%7CUSD%7C840; skt=bd11359560e75d95; csg=a0f1fd9e; uc3=vt3=F8dByR6tG%2Fo8%2BTMkhA0%3D&id2=UU2zWEY83QvJUw%3D%3D&nk2=Dl9OSuEBXckgvrMDjw%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU0MjU4MTEyMw%3D%3D; _cc_=UtASsssmfA%3D%3D; mt=ci=0_1&np=; l=Ajg4Un6m2WRL3bhdrFTvEj38iO3LtJwr; uc1=cookie14=UoTYNOpM4LIK%2Bg%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=VFC%2FuZ9aj3yE&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; isg=BHx8itNTC_65vT8i7YE1VTr3TRzu3SD4ulu6rlb9iGdKIRyrfoXwL_KTBBH8bFj3'
    cookies = {}
    for line in coo.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    kv = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url, kv, cookies)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
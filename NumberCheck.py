import os
import requests
from lxml import etree
#抓取当前中奖号码
url = 'http://kaijiang.500.com/dlt.shtml'
response = requests.get(url)
txt = response.text
html = etree.HTML(txt)
redresult = html.xpath('//ul/li[@class="ball_red"]/text()')
blueresult = html.xpath('//ul/li[@class="ball_blue"]/text()')
noresult = html.xpath('//font[@class="cfont2"]/strong/text()')
def check(list,redresult,blueresult):
    rlist=list[0:5]
    blist=list[5:7]
    rcnt = 0
    bcnt = 0
    for e in redresult:
        if int(e) in rlist:
            rcnt= rcnt+1
    for e in blueresult:
        if int(e) in blist:
            bcnt = bcnt+1
    # print('红球命中'+str(rcnt)+'，蓝球命中'+str(bcnt))
    if (rcnt == 5 and  bcnt == 2):return 100000000
    elif (rcnt == 5 and  bcnt == 1):return 200000
    elif (rcnt == 5 and bcnt == 0):return 10000
    elif (rcnt == 4 and bcnt == 2):return 3000
    elif (rcnt == 4 and bcnt == 1):return 300
    elif (rcnt == 3 and bcnt == 2):return 200
    elif (rcnt == 4 and bcnt == 0):return 100
    elif (rcnt == 2 and bcnt == 2):return 15
    elif (rcnt == 3 and bcnt == 1):return 15
    elif (rcnt == 1 and bcnt == 2):return 5
    elif (rcnt == 3 and bcnt == 0):return 5
    elif (rcnt == 2 and bcnt == 1):return 5
    elif (rcnt == 0 and bcnt == 2):return 5
    else:return 0
list1 = []
print('中奖号码:')
print(redresult)
print(blueresult)
n=int(input('请输入购买注数'))
print('请输入你的球号')
checklist = []
for i in range(0,n,1):
    list1=input().split()
    list = []
    for e in list1:
        list.append(int(e))
    money = check(list,redresult,blueresult)
    checklist.append(money)
print('第'+noresult[0]+'期'+'你的中奖情况如下')
print(checklist)
os.system("pause")
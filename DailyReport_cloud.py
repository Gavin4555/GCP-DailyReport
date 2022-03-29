# -*- coding:utf-8 -*-
import requests
import json
import urllib.parse

class report:
    '''
    构造函数
    '''
    def __init__(self,n,s):
        name=str(n)
        self.name=name
        self.switch=s
        self.read()
        self.start()
        if self.switch==1:
            self.push()
    

    '''
    数据初始化处理
    '''
    def read(self):
        c = open('./'+self.name+'.txt')
        data0 = c.readline()
        c.close()
        data0 = str(data0).replace('&', '","')
        data0 = '{"'+data0.replace('\n','"').replace('=','":"')+'"}'
        data0=json.loads(data0)
        self.data0=data0


    '''
    推送
    '''
    def push(self):
        token=self.data0['token']
        title1="每日一报——用户："+ self.name +"，填报成功"
        title0="每日一报——用户："+ self.name +"，填报失败！请手动填报"
        title="每日一报——用户："+ self.name +"，填报失败！请手动检查"
        if self.status_code==200 :
            if self.result['msg']=="保存成功" :
                print("用户："+self.name+"——填报成功，开始推送...")
                p = requests.get('http://www.pushplus.plus/send?token='+token+'&title='+title1+'&content='+'msg:'+self.result['msg']+'&template=html')
                #print(p.text)
            else:
                print("用户："+self.name+"——填报失败！开始推送...")
                p = requests.get('http://www.pushplus.plus/send?token='+token+'&title='+title0+'&content='+'msg:'+self.result['msg']+'&template=html')
                #print(p.text)
        else:
            print("用户："+self.name+"——填报失败！开始推送...")
            p = requests.get('http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+self.result['msg']+'&template=html')
        print("-----------------push--------------------")
        print(p.text)


    '''
    填报
    '''
    def start(self):
        url = 'https://g.hc-web.cn/api/index/putNewDay'
        header = {
            'Host':'g.hc-web.cn',
            'Connection':'keep-alive',
            'Content-Length':'939',
            'content-type':'application/x-www-form-urlencoded',
            'Accept-Encoding':'gzip,compress,br,deflate',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123a) NetType/WIFI Language/zh_CN',
            'Referer':'https://servicewechat.com/wxa94aa0baa78ebdb9/59/page-frame.html'
        }
        payload ={
        "uid":self.data0['uid'],
        "is_campus":urllib.parse.unquote(self.data0['is_campus']),
        "campus":urllib.parse.unquote(self.data0['campus']),
        "nowaddress":urllib.parse.unquote(self.data0['nowaddress']),
        "nowaddressinfo":urllib.parse.unquote(self.data0['nowaddressinfo']),
        "region_address":urllib.parse.unquote(self.data0['region_address']),
        "phone":urllib.parse.unquote(self.data0['phone']),
        "fever":urllib.parse.unquote(self.data0['fever']),
        "feverinfo":urllib.parse.unquote(self.data0['feverinfo']),
        "feverinfo1":urllib.parse.unquote(self.data0['feverinfo1']),
        "feverinfo2":urllib.parse.unquote(self.data0['feverinfo2']),
        "feverinfo3":urllib.parse.unquote(self.data0['feverinfo3']),
        "jie":urllib.parse.unquote(self.data0['jie']),
        "jie1":urllib.parse.unquote(self.data0['jie1']),
        "jie3":urllib.parse.unquote(self.data0['jie3']),
        "jie4":urllib.parse.unquote(self.data0['jie4']),
        "jie5":urllib.parse.unquote(self.data0['jie5']),
        "jie6":urllib.parse.unquote(self.data0['jie6']),
        "jie7":urllib.parse.unquote(self.data0['jie7']),
        "jie8":urllib.parse.unquote(self.data0['jie8']),
        "jie9":urllib.parse.unquote(self.data0['jie9']),
        "jie10":urllib.parse.unquote(self.data0['jie10']),
        "jie11":urllib.parse.unquote(self.data0['jie11']),
        "plan":urllib.parse.unquote(self.data0['plan']),
        "planaddress":urllib.parse.unquote(self.data0['planaddress']),
        "risk_area":urllib.parse.unquote(self.data0['risk_area']),
        "risk_area_address":urllib.parse.unquote(self.data0['risk_area_address']),
        "jkcode":urllib.parse.unquote(self.data0['jkcode']),
        "new_status":urllib.parse.unquote(self.data0['new_status']),
        "status_remark":urllib.parse.unquote(self.data0['status_remark']),
        "company":urllib.parse.unquote(self.data0['company']),
        "city":urllib.parse.unquote(self.data0['city']),
        "other_status":urllib.parse.unquote(self.data0['other_status']),
        }
        r = requests.request('post', url, data=payload, headers=header)
        result=json.loads(r.text)
        self.result=result
        self.status_code=r.status_code
        print("-----------------report_status--------------------")
        print(r.text)
        print(r.status_code)


'''
入口
'''
def main(event,content):
    report('歪比巴卜',1)
# Version: 2.2
# Author: Huxin
import requests
import sys
import io
import os

class stats:
    uid=0;name='';color='';ccfLevel=0;badge='';passed=[];submitted=[];passedNum=0;unpassedNum=0

class mainPart: # 主要函数类
    # ===== 初始化信息 =====
    
    def init():  # 处理 uid
        try:
            uid=input('Please input the user id in Luogu: ').split()
            for i in range(len(uid)):
                uid[i]=int(uid[i])
            return uid
        except:
            print('Please input the correct uid!')
            sys.exit()
    
    def crawl(uid): # 爬取用户信息
        global response
        url='https://www.luogu.com.cn/user/'+str(uid)+'?_contentOnly'
        headers={
            'User-Agent':\
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        response=requests.get(url=url,headers=headers)
        
    def getInfo(): # 将信息转换为内部变量
        res=response.json()
        stats.user=res['currentData']['user']
        try:
            stats.passed=res['currentData']['passedProblems']
            stats.submitted=res['currentData']['submittedProblems']
        except:
            stats.passed=[]
            stats.submitted=[]
            stats.hideInfo=True
        else:
            stats.hideInfo=False
        stats.uid=int(stats.user['uid'])
        stats.name=stats.user['name']
        stats.color=stats.user['color']
        stats.ccfLevel=stats.user['ccfLevel']
        stats.badge=stats.user['badge']
        try:
            stats.passedNum=int(stats.user['passedProblemCount'])
            stats.submittedNum=int(stats.user['submittedProblemCount'])
            stats.unpassedNum=int(len(stats.submitted))
        except:
            stats.passedNum=0
            stats.submittedNum=0
            stats.unpassedNum=0
            stats.hideInfo=True
    
    # ===== 输出具体信息 ===== #
    
    def getListJson(): # list.json
        f=open(str(stats.uid)+'/accepted/list.json','w',encoding='utf-8')
        f.write('{\n')
        f.write(tools.isGetted())
        f.write('    \"acceptedNumber\": '+str(len(stats.passed))+',\n')
        f.write('    \"list\": [')
        for i in range(len(stats.passed)):
            f.write(str('\"'+stats.passed[i]['pid']+'\"'))
            f.write(tools.isComma(i))
        f.write(']\n}\n')
        f.close()
    
    def getListText(): # list.txt
        f=open(str(stats.uid)+'/accepted/list.txt','w',encoding='utf-8')
        f.write('{\n')
        for i in range(len(stats.passed)):
            f.write(str('['+stats.passed[i]['pid']+']'))
            f.write(tools.isComma(i)); f.write(tools.isNewline(i))
        f.write('\n}\n')
        f.close()
    
    def getDetailText(): # detail.txt
        f=open(str(stats.uid)+'/accepted/detail.txt','w',encoding='utf-8')
        for i in range(len(stats.passed)):
            f.write(str('['+stats.passed[i]['pid']+' '+\
                    tools.Title(stats.passed[i]['title'])+']'))
            f.write(tools.isComma(i)); f.write('\n')
        f.close()
    
    def getDictJson(): # dict.json
        f=open(str(stats.uid)+'/accepted/dict.json','w',encoding='utf-8')
        f.write('{\n')
        f.write(tools.isGetted())     # "isGetted": true/false,
        f.write('    \"acceptedNumber\": '+str(len(stats.passed))+',\n')     # 通过数量
        f.write('    \"problems\": [\n')     # 建立 problem 列表
        for i in range(len(stats.passed)):     # 完隐用户无法获取，即 len(stats.passed)=0
            f.write('    {\"pid\":\"'+stats.passed[i]['pid']+'\",\"title\":\"'+\
                    tools.Title(stats.passed[i]['title'])+'\"}')
            f.write(tools.isComma(i)); f.write('\n')     # 处理逗号，输出换行
        f.write('    ]\n}\n')
        f.close()

    # ===== 主函数 ======
    
    def main():
        uidList=mainPart.init() # 读入 uid
        for i in range(len(uidList)):
            tools.dealOS(uidList[i]) # 初始化文件夹
            mainPart.crawl(uidList[i]) # 爬取该用户个人信息
            mainPart.getInfo() # 将爬取内容转换为内部变量
            mainPart.getListText() # 输出 list.txt
            mainPart.getListJson() # 输出 list.json
            mainPart.getDetailText() # 输出 detail.txt
            mainPart.getDictJson() # 输出 dict.json

class tools:
    # ===== 一些工具函数 =====
    
    def Title(s): # 判断题目标题是否合法
        if s.count('\"')==0: # 是否有 " 在标题内
            return s
        else:
            return 'UnknownTitle'
    def isGetted(): # 返回该用户是否开完全隐藏
        if stats.hideInfo:
            return '    \"isGetted\": false,\n'
        else:
            return '    \"isGetted\": true,\n'
    def isComma(x): # 返回当前状态下，是否需要输出逗号
        if x!=len(stats.passed)-1:
            return ','
        else:
            return ''
    def isNewline(x): # 返回当前状态下，是否需要换行（仅用于 list.txt）
        if (x+1)%10==0: # 十个一行
            return '\n'
        else: # 非结尾，不需要换行
            return ''
    def dealOS(uid): # 判断 /uid/accepted 文件夹是否存在并建立
        if not os.path.exists(str(uid)):
            os.makedirs(str(uid))
        if not os.path.exists(str(uid)+'/accepted'):
            os.makedirs(str(uid)+'/accepted')

if __name__ == '__main__':
    mainPart.main()

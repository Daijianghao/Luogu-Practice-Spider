#define VERSION rc 1.1.0
import requests
import sys
import io
import os
uid=int(input())
url='https://www.luogu.com.cn/user/'+str(uid)+'?_contentOnly'
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
response = requests.get(url=url,headers=head)
#out=str(response.text).encode('utf-8').decode('unicode_escape')
res=response.json()
user=res['currentData']['user']
passed=res['currentData']['passedProblems']
submitted=res['currentData']['submittedProblems']

class stats:
    uid=uid
    name=user['name']
    color=user['color']
    ccflevel=user['ccfLevel']
    tag=user['badge']
    passed_num=int(user['passedProblemCount'])
    submitted_num=int(user['submittedProblemCount'])
    unpassed_num=int(len(submitted))
    hideinfo=False
if passed:
    stats.hideinfo=True


if not os.path.exists(str(uid)):
        os.makedirs(str(uid))
f=open(str(uid)+'/accepted_list.json','w',encoding='utf-8')
f.write('{\n')
f.write('    \"Accepted_number\": '+str(stats.passed_num)+',\n')
f.write('    \"list\": [')
for i in range(stats.passed_num):
    f.write(str('\"'+passed[i]['pid']+'\"'))
    if not i==stats.passed_num-1:
        f.write(',')
f.write(']\n}\n')
f.close()

f=open(str(uid)+'/accepted_list.txt','w',encoding='utf-8')
f.write('{\n')
for i in range(stats.passed_num):
    f.write(str('['+passed[i]['pid']+']'))
    if not i==stats.passed_num-1:
        f.write(',')
    if (i+1)%10==0:
        f.write('\n')
f.write('\n}')
f.close()

f=open(str(uid)+'/accepted_detail.txt','w',encoding='utf-8')
for i in range(stats.passed_num):
    if str(passed[i]['title']).count('\"')==0:    
        f.write(str('['+passed[i]['pid']+' '+passed[i]['title']+']'))
    else:
        f.write(str('['+passed[i]['pid']+' '+'Uknown title]'))
    if not i==stats.passed_num-1:
        f.write(',')
    f.write('\n')
f.close()

f=open(str(uid)+'/accepted_dict.json','w',encoding='utf-8')
f.write('{\n')
f.write('    \"Accepted_number\": '+str(stats.passed_num)+',\n')
f.write('    \"problems\":[\n')
for i in range(stats.passed_num):
    if str(passed[i]['title']).count('\"')==0:
        f.write('    {\"pid\":\"'+passed[i]['pid']+'\",\"title\":\"'+passed[i]['title']+'\"}')
    else:
        f.write('    {\"pid\":\"'+passed[i]['pid']+'\",\"title\":\"'+'Unknown_title'+'\"}')
    if not i==stats.passed_num-1:
        f.write(',')
    f.write('\n')
f.write('    ]\n}\n')
f.close()

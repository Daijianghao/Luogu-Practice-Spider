### Luogu-Practice-Spider 洛谷练习爬虫

Crawling the practice list on the user on Luogu.

It's updating.

#### Development team list

| <img src="https://avatars.githubusercontent.com/u/70331183?v=4" width="60px"></br> Huxin
| :---: |
| ![](https://shields.io/badge/admin-red?logo=microsoftteams&style=for-the-badge) <br> ![](https://shields.io/badge/Coding-green?logo=visual-studio-code&style=for-the-badge)<br> ![](https://shields.io/badge/BugTester-yellow?logo=open-bug-bounty&style=for-the-badge) <br> ![](https://shields.io/badge/Issues%20Manager-green?logo=visual-studio-code&style=for-the-badge)|
---

#### How to use it

Download `index.py`.Run it with your method.

Input the user id on Luogu(which is a number)，**It can not obtain the user which is open the mode 'complete privacy' on Luogu**.

If the user which you input haven't open the 'complete privacy',you will get the files as follows in `[uid]/`:

#### One. `accepted_list.json`

It's a `json` file,accepted problems and accepted problem id of the user in it.

```
{
    "Accepted_number": 603,
    "list": ["P1001","P7866",...]
}
```

#### Two. `accepted_list.txt`

Input the practise like the website on Luogu,which is ten problem in one line.

```
{
    [P1001],[P1002],[P1003],[P1004],[P1007],[P1008],[P1009],[P1012],[P1014],[P1020],
    [P1024],[P1025],[P1028],[P1029],[P1030],[P1031],[P1035],[P1036],[P1042],[P1044],
    ...
}
```

#### Three. `accepted_detail.txt`

Write the text which is the problem id and title of a line.

```
[P1001 A+B Problem],
[P1002 [NOIP2002 普及组] 过河卒],
[P1003 [NOIP2011 提高组] 铺地毯],
...
```

#### Four. `accepted_dict.json`

Complete `json` file of the user's practice.

```
{
    "problems":[
    {"pid":"P1001","title":"A+B Problem"},
    {"pid":"P1002","title":"[NOIP2002 普及组] 过河卒"},
    {"pid":"P1003","title":"[NOIP2011 提高组] 铺地毯"},
    {"pid":"P1004","title":"[NOIP2000 提高组] 方格取数"},
    {"pid":"P1005","title":"[NOIP2007 提高组] 矩阵取数游戏"}
    ]
}
```

### Luogu-Practice-Spider 洛谷练习爬虫

——Know yourself and know your enemy, and be in the palm of your hand.

Crawling user's practice on Luogu.

**Please use this script reasonably. I am not responsible for the consequences.**

Ongoing update.

Lastest version: [v2.2](https://github.com/Daijianghao/Luogu-Practice-Spider/releases/tag/v2.2)。

**English** | [简体中文](https://github.com/Daijianghao/Luogu-Practice-Spider/blob/Ver-2.2/README.md)

If you find it useful, please give me a free star, thanks \>\_\<.

#### Development team list

| <img src="https://avatars.githubusercontent.com/u/70331183?v=4" width="60px"></br> Huxin
| :---: |
| ![](https://shields.io/badge/admin-red?logo=microsoftteams&style=for-the-badge) <br> ![](https://shields.io/badge/Coding-green?logo=visual-studio-code&style=for-the-badge)<br> ![](https://shields.io/badge/BugTester-yellow?logo=open-bug-bounty&style=for-the-badge) <br> ![](https://shields.io/badge/Issues%20Manager-green?logo=visual-studio-code&style=for-the-badge)|
---

#### How to use it

Download `index.py`. Run it with your method.

Before that, you must configure the python environment and install the `requests` library.

If you have configured pip, you need to enter `pip install requests` in the terminal.

After running, enter the user uid of Luogu. Note that **the detailed practice of completely hiding the user cannot be obtained**.

If the crawled object is not fully hidden, you will get the following things in the same directory of `[uid]/accepted` :

#### One. `list.json`

It's a `json` file, accepted problems and accepted problem id of the user in it.

```
{
    "Accepted_number": 603,
    "list": ["P1001","P7866",...]
}
```

#### Two. `list.txt`

Output the practise like the practice website on Luogu, which is ten problem in one line.

```
{
    [P1001],[P1002],[P1003],[P1004],[P1007],[P1008],[P1009],[P1012],[P1014],[P1020],
    [P1024],[P1025],[P1028],[P1029],[P1030],[P1031],[P1035],[P1036],[P1042],[P1044],
    ...
}
```

#### Three. `detail.txt`

Write the text which is the problem id and title of a line.

```
[P1001 A+B Problem],
[P1002 [NOIP2002 普及组] 过河卒],
[P1003 [NOIP2011 提高组] 铺地毯],
...
```

#### Four. `dict.json`

Complete `json` file of the user's practice.

In case of conflict or dispute between different formats, it is recommended to use this dictionary as the main one.

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

#### Five. Main purpose:

+ You can crawl your own practice every other week / month to compare, understand and supervise yourself.

+ You can also crawl through the practice records of your classmates / teachers to find out what is missing and make progress together.

+ Examples of comparison can be expanded and viewed in [the new version of PR](https://github.com/Daijianghao/Luogu-Practice-Spider/pull/4/files).

[![jIizkj.png](https://s1.ax1x.com/2022/07/17/jIizkj.png)](https://imgtu.com/i/jIizkj)


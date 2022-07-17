### Luogu-Practice-Spider 洛谷练习爬虫

——知己知彼，控于掌中。

爬取洛谷用户练习情况。

**请合理运用此脚本，出现的后果本人概不负责。**

持续更新中。

最新版本：[v2.1](https://github.com/Daijianghao/Luogu-Practice-Spider/releases/tag/v2.1)。

[English](https://github.com/Daijianghao/Luogu-Practice-Spider/blob/main/README.en-Hans.md) | **简体中文**

#### 开发组名单

| <img src="https://avatars.githubusercontent.com/u/70331183?v=4" width="60px"></br> Huxin
| :---: |
| ![](https://shields.io/badge/admin-red?logo=microsoftteams&style=for-the-badge) <br> ![](https://shields.io/badge/Coding-green?logo=visual-studio-code&style=for-the-badge)<br> ![](https://shields.io/badge/BugTester-yellow?logo=open-bug-bounty&style=for-the-badge) <br> ![](https://shields.io/badge/Issues%20Manager-green?logo=visual-studio-code&style=for-the-badge)|
---

#### 使用方法

下载 `main.py` 并运行。

在这之前，您必须配置 python 环境，并且安装 `requests` 库。

如果您已经配置好了 pip，您需要在终端内输入 `pip install requests`。


运行后输入洛谷用户 uid，**无法获取完全隐藏用户的详细练习**。

如果对象没开完隐，你将在同目录下 `[uid]/accepted` 得到：


#### 一、 `list.json`

`json` 文件，将输出 通过题目数量 和 通过题目题号。

```
{
    "isGetted": true,
    "acceptedNumber": 603,
    "list": ["P1001","P7866",...]
}
```

#### 二、 `list.txt`

输出类似于洛谷练习情况的文本文档。十个题号一换行。

```
{
    [P1001],[P1002],[P1003],[P1004],[P1007],[P1008],[P1009],[P1012],[P1014],[P1020],
    [P1024],[P1025],[P1028],[P1029],[P1030],[P1031],[P1035],[P1036],[P1042],[P1044],
    ...
}
```

#### 三、 `detail.txt`

输出带题号和题目名称的文本文档。一题一行。

```
[P1001 A+B Problem],
[P1002 [NOIP2002 普及组] 过河卒],
[P1003 [NOIP2011 提高组] 铺地毯],
...
```

#### 四、 `dict.json`

最标准的完整 `json` 字典。

当不同格式出现冲突或争议时，建议以此字典为主。

```
{
    "isGetted": true,
    "acceptedNumber": 603,
    "problems": [
    {"pid":"P1001","title":"A+B Problem"},
    {"pid":"P1002","title":"[NOIP2002 普及组] 过河卒"},
    {"pid":"P1003","title":"[NOIP2011 提高组] 铺地毯"},
    {"pid":"P1004","title":"[NOIP2000 提高组] 方格取数"},
    {"pid":"P1005","title":"[NOIP2007 提高组] 矩阵取数游戏"}
    ]
}
```

#### 五、主要应用

+ 可每隔一周/一月爬取一次自己的练习情况，进行比对，了解并督促自己。
+ 也可爬取同学/老师的练习记录，差缺不漏，一起进步。
+ 比较情况示例可于 [新版本 PR](https://github.com/Daijianghao/Luogu-Practice-Spider/pull/4/files) 中展开查看。

[![jIizkj.png](https://s1.ax1x.com/2022/07/17/jIizkj.png)](https://imgtu.com/i/jIizkj)

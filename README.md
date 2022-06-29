### Luogu-Practice-Spider 洛谷练习爬虫

爬取洛谷用户练习情况。

持续更新中。

#### 开发组名单

| <img src="https://avatars.githubusercontent.com/u/70331183?v=4" width="60px"></br> Huxin
| :---: |
| ![](https://shields.io/badge/admin-red?logo=microsoftteams&style=for-the-badge) <br> ![](https://shields.io/badge/Coding-green?logo=visual-studio-code&style=for-the-badge)<br> ![](https://shields.io/badge/BugTester-yellow?logo=open-bug-bounty&style=for-the-badge) <br> ![](https://shields.io/badge/Issues%20Manager-green?logo=visual-studio-code&style=for-the-badge)|
---

#### 使用方法

下载 `index.py` 并运行。

输入洛谷用户 uid，**无法获取完全隐藏的用户练习请看**。

如果对象没开完隐，你将在同目录下 `[uid]/` 得到：


#### 一、 `accepted_list.json`

`json` 文件，将输出 通过题目数量 和 通过题目题号。

```
{
    "Accepted_number": 603,
    "list": ["P1001","P7866",...]
}
```

#### 二、 `accepted_list.txt`

输出类似于洛谷练习情况的文本文档。十个题号一换行。

```
{
    [P1001],[P1002],[P1003],[P1004],[P1007],[P1008],[P1009],[P1012],[P1014],[P1020],
    [P1024],[P1025],[P1028],[P1029],[P1030],[P1031],[P1035],[P1036],[P1042],[P1044],
    ...
}
```

#### 三、 `accepted_detail.txt`

输出带题号和题目名称的文本文档。一题一行。

```
[P1001 A+B Problem],
[P1002 [NOIP2002 普及组] 过河卒],
[P1003 [NOIP2011 提高组] 铺地毯],
...
```

#### 四、 `accepted_dict.json`

正经的完整 `json` 字典。

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

# Class Management System
----
> 基于Django框架搭建的管理系统

----
## 完成步骤：
1. 按需求更改前端html5、css和javasript（css和javascript不需要过多修改）
2. 后台数据处理模块完成

----
注意事项：
* html5文件在项目文件的templates文件夹中，css和javascript文件是静态文件，在static文件夹目录中
* 为防止更改出错，我在github repository根目录留了html5模板的备份
* 前端设计是主要内容，需要根据不同的班委设计不同的界面
* 由于服务器是linux系统，文件管理系统不太一样，项目可能在win上无法正常运行（我没试过呜呜呜）
* 服务器网址：121.4.214.125，端口号我运行的时候通常设置为8000

----
目前已完成html5文件更改：
1. pages-signin 登陆界面
2. pages-changeid 更改密码界面

----
目前已完成数据处理：
1. 登陆（完全实现）
2. 更改密码（完全实现）

----
需要在DDL前实现的功能（有待完善）：  
~~1. 登陆~~  
~~2. 更改密码~~  
~~3. 主页~~  
4. 通知&消息
5. 提交作业  
6. 班级Gallery  
7. 提交获奖信息  
8. 活动分查看  
9. 班级管理  

----
需要的界面：  
序号|界面名称|界面信息
:--:|:--:|:--:
1|登陆界面| pages-signin.html 已完成
2|更改密码界面| pages-changeid.html 已完成
3|主界面| mainpage.html 已完成（需要添加图片）
4|通知-作业通知| messages_homework.html 已完成
5|通知-比赛通知| messages_competition.html 已完成
6|通知-活动通知| messages_activity.html 已完成
7|通知-通知消息| messages_message.html 已完成
8|通知-通知内容界面| homework_message.html <br />competition_message.html <br />activity_message.html <br />已完成
9|作业DDL一览|--
10|作业DDL一览-作业提交界面|--
11|我提交的作业|--
12|班级Gallery-班级成员|--
13|班级Gallery-班级委员|可参考班级成员
14|提交获奖信息|--
15|奖项审核进度|可参考作业通知
16|审核通过的奖项|可参考作业通知
17|活动分查看|--
18|发布通知-发布比赛通知| competition_upload.html 已完成
19|发布通知-发布活动通知| activity_upload.html 已完成
20|发布通知-发布作业通知| homework_upload.html 已完成
21|通知反馈|--
22|奖项审核-奖项一览|--
23|奖项审核-审核界面|--
23|活动分统计|可参考活动分查看

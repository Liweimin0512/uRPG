# 《创世物语》

利用 UE4 + KBEngine 开发的MMORPG游戏Demo
[EnglishDoces](https://github.com/Liweimin0512/uRPG/blob/master/Manage/CreationStory.md)

## 游戏概述

游戏名：《创世物语》（暂定）（备选名：《未至之境》）

游戏中玩家扮演的角色穿梭在各个风格迥异的的世界之间，给这些蛮荒世界带去秩序。并改造世界。

## 技术选型

* 前端  ：UE        4.22.3
* 后端  ：KBEngine  2.5.7
* 数据库：mysql     8.0.17
* VisualStudio 2019

主要是考虑到后期要进行Linux系统上服务器的部署
建议围观的小伙伴采用和我相同的版本运行项目。

目前Server目录已经使用git子模块,地址：[UPRG-Server](https://github.com/Liweimin0512/URPG-Server)

## UE4插件

* Victory插件，一个功能扩展函数库
* GameplayAbilities插件，官方提供的能力系统

## 分支描述

* master 主分支，保证最新的可运行版本
* release 发布分支，保证最新的可发布版本
* dev 开发分支，保证最新的开发内容
* bug debug分支，游戏中问题改正专用

## 目录结构

* Asset         美术资源暂存目录，客户端可执行文件暂存处
* Client        客户端项目所在位置
* ConfigTable   游戏数据配置表所在位置
* Design        设计文档
* Manage        管理目录，暂时项目只我一个人所以没用
* Server        服务器项目所在位置
* Tools         其他开发工具

## 目前进度

这部分暂时删除，每个版本目标不同，进度也无法确定。
具体可以查看Manage目录下

## 参与人员

目前只有我一个人，有小伙伴想参与的联系我！

## 开发日志

本项目开发日志请关注本人的知乎专栏：[《创世物语》开发日志文字版](https://zhuanlan.zhihu.com/c_1151855724538703872)
视频版本的开发日志请关注本人的B站主页：[《创世物语》开发日志视频版](https://space.bilibili.com/8618918)

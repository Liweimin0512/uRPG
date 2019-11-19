# 创建角色界面

## 界面控件

- [Text]race_name种族名称
- [Text]race_info种族简介
- [Image]skill技能图标（1~3）
- [Image]talent天赋图标（1~2）
- [button]种族选择左右翻页按钮
- [button]发型选择左右翻页按钮
- [button]脸型选择左右翻页按钮
- [text_editor]avatar_name角色名称
- [button]clance取消创建
- [button]create确认创建

## 界面初始化

默认选择第一个种族
根据配置表中信息，显示在界面上种族名称、种族介绍
根据配置表中信息，更新BP_SelectedAvatar
判断当前账号角色数量是否<=0、若为真，则隐藏取消按钮

## 种族选择（左右翻页）

- 根据选择种族更新界面显示信息（种族名、种族简介、预设技能及天赋等）
- 发型重置为1
- 脸型重置为1
- 更新BP_seletedAvatar模型

## 发型选择（左右翻页）

- 角色发型ID增减
- 更新BP_seletedAvatar模型

## 脸型选择（左右翻页）

- 角色脸型ID增减
- 更新BP_seletedAvatar模型

## 取消创建

关闭创建角色界面并打开选择角色界面

## 确认创建

获取当前avatar_name和raceID来请求创建角色

# 道具系统

## 道具属性

变量名	变量类型	字段名	解释说明
id	int	id	道具全局唯一标识
name	String	名称	名称KEY
type	int	类型	类型，索引到Item_type表
type_child	int	子类型id	子类型
bind_type	int	是否绑定	是否为绑定道具：绑定道具不能交易
stack_limit	int	堆叠数量	超上限则占用另一个背包格
itemicon	int	图标id	索引到item_pic表
itemcolor	int	品质	灰白绿蓝紫橙红
item_recycle	int	分解产物	索引到道具分解表
weight	int	重量	负重系统需要的数值
durability	int	耐久	索引到耐久表
sub_job_limit	int	副职业限制	为空则不受限制
level_limit	int	等级限制	为空则不受限制
time_limit	int	时间限制	单位：min
use_id	int	使用方案	索引use_list表
info_text	String	说明文本	说明KEY
auction_level	int	交易级别	拍卖行级别(0不能上拍卖行，1低级市场，2高级市场)
get_approach	int	获取途径	
active_time	int	有效时间	单位s，随服务器计时，时间结束时扣除道具
mission_ID	int	关联任务	查找任务表

## 使用类型

- 获得奖励：最基础的道具需求，宝箱类道具通常会在使用时获得奖励（甚至触发掉落）
- 使用技能：通常是给自己添加某种BUFF或者给目标添加某种BUFF，这时候道具可以作为技能的入口处理（道具的冷却时间就是技能的冷却时间）
- 触发脚本：一些应用更少的情况，特别是在任务中可能需要道具召唤怪物、触发过场动画等，这时就需要脚本功能的支持

## 武器装备

- 装备位:不填则表示不可以装备，包括如下几种装备位：
  - 帽子
  - 衣服
  - 裤子
  - 鞋子
  - 手套
  - 主手：是武器
  - 副手：是武器
  - 其他（盾牌位置）

道具装备后根据所在装备位，分别在equip和weapon表中找到相关数据，并进行相关操作

## 装备equip

一个道具是装备，则具有以下属性：

- 装备时触发事件
- 卸载时触发事件
- 装备后提供的属性值，索引到属性表

## 武器weapon

武器除装备包含的属性外，还包含武器类型的区别，武器类型不同，决定了装备武器时动作、普通攻击技能及其他。
目前武器类型包括：

- 刀
- 枪
- 剑
- 其他

## 道具标签

道具标签方便在针对标签进行筛选时操作，标签不是唯一的。

- 装备
- 商品
- 任务道具
- 消耗品


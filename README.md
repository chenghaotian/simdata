# 数据分析及随机数据生成程序

#### 介绍
- 基于Python数学数据分析(datana)
- 基于Python数学数据模拟(sim)

#### 作者
- 成昊天

#### 联系方式
- Email:dboycht@qq.com
- Github:[Github](http://github.com/chenghaotian)

### 更新日志 
#### v1.0
- 编写日期: _Dec.18/2022_
- 发布初代版本库
- 使用说明: 
  - datana.py 
    - 主程序: main(datas: list) 
      - 变量 datas: 传入的数据(列表内只能是int 格式)
      - 返回 类型为列表
        - 元素为 "平均数 方差 极差 最大 最小"
  - sim.py
    - 主程序: main(da_list: list, cir_nu: int, data_length: int):
      - 变量 
        - da_list: 每轮的物品状态
        - cir_nu: 抽多少轮
        - data_length: 每轮抽取个数+1
      - 返回 dict
        - 类型 dict(str: list(str))
        - 数据 字典(序列号: 每轮空间(模拟空间样本))

#### v1.1
- 编写日期: _Dec.19/2022_
- 使用说明: 
  - datana.py
    - 主程序: main(datas: list) 
      - 变量 datas: 传入的数据(列表内只能是int 格式)
      - 返回 list
        - 类型 list(float, float, int/float,  int/float, int/float, list(int/float))
        - 数据 列表(平均数 方差 极差 最大 最小 从小到大)
  - sim.py
    - **存在重大bug 预计1.2修复**

#### v1.11
- 编写日期: _Dec.19/2022_
- 更新了README文档

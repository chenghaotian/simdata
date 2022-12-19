# -*- coding:utf-8 -*-
"""
作者:成昊天
更新日志
# v1.0
  发布首个版本
# v1.1
  Date:2022年12月19日
  更新了录入功能和排序
"""


def main(datas: list):
    # 仅支持列表中为int
    da_copy = datas
    he = 0
    he2 = 0
    for he1 in da_copy:
        he += he1
        he2 += (he1 * he1)
    average = he / (len(da_copy))
    rang = max(da_copy) - min(da_copy)
    var = (he2 / len(da_copy)) - average * average
    lh = sorted(da_copy, reverse=False)
    return [average, var, rang, max(da_copy), min(da_copy), lh]  # 平均数 方差 极差 最大 最小 低至高


if __name__ == '__main__':
    print("当前版本: v1.1")
    data = []
    while True:
        q = input("输入数据(回车结束):")
        if q == "":
            break
        else:
            data.append(int(q))
    rt = main(data)
    print(f"平均数:{rt[0]}\n"
          f"方差:{rt[1]}\n"
          f"极差:{rt[2]}\n"
          f"最大值:{rt[3]}\n"
          f"最小值:{rt[4]}\n")
    lth = rt[5]
    q = 1
    print("编号: 值")
    for read in lth:
        print(f"{q}:{lth[q-1]}")
        q += 1

# -*- coding:utf-8 -*-
# shujufenxi数据分析

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
    return [average, var, rang, max(da_copy), min(da_copy)]  # 平均数 方差 极差 最大 最小


if __name__ == '__main__':
    print(main([1, 2, 3, 4]))

# -*- coding: utf-8 -*-
import random


def main(da_list: list, cir_nu: int, data_length: int):
    # 数据池 数据单元数 单元抽取个数+1
    a = {}
    da_list_2 = da_list
    for i in range(0, cir_nu):
        olist = list(da_list_2)
        dom = []
        for k in range(0, data_length):
            root = random.randint(0, len(olist)-1)
            dom.append(olist[root])
            olist.pop(root)
        a[str(i)] = dom
    return a


if __name__ == '__main__':
    a_l = []
    while True:
        k = input("有哪几个状态?")
        if k == '':
            break
        a_l.append(k)

    file = main(a_l, int(input("多少次"))+1, int(input("单次抽取个数")))
    for a in range(0, len(file)-1):
        print(file[str(a)])

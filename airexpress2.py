import sys
import re

class Data:
    exchange_rate = 7
    discount = 0.65
    product_title = None
    final_price = None
    product_name = None
    china_price = None
    product_price = None
    weight = None
    freight_charges = None
    china_product_url = None
    profit = None
    shippment_charge = None
    opponent_price = None
    promotion_cost = None
    airexpress_commission = None
    Feature = None
    Specication = None
    shippment_charge_judge = None

    def get_information(self):

        print("请输入商品名称:")
        Data.product_name = input()

        print("请输入产品标题")
        Data.product_title
        product_title = sys.stdin.readline()
        print('标题字符串的个数是：', len(product_title), '个')
        product_title1 = re.compile(r'\b[a-zA-Z]+\b', re.IGNORECASE).findall(product_title)
        # 将列表中的大写字母转换成小写
        # 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法
        product_title2 = [s.lower() for s in product_title1 if isinstance(s, str) == True]
        print(product_title2)
        for i in product_title2:
            count = product_title2.count(i)
            print('标题中每个单词的出现次数是:')
            print(i, ':', count)
            if count >= 3:
                print("出现标题关键词次数违规：")
                print(i, ':', count)
                exit()

    def get_caculate_information(self):
        print('请输入重量:')
        Data.weight = input()

        print("请输入物流价格:")
        Data.freight_charges = float(input())

        print("请输入拿货价格:")
        Data.china_price = float(input())

        print("请输入目标利润:")
        Data.profit = float(input())

        print("请输入货源url")
        Data.china_product_url = input()

        print("对手是否包邮(0包邮/1不包邮)：")
        Data.shippment_charge_judge = input()
        if int(Data.shippment_charge_judge) == 1:
            print('请输入邮费：')
            Data.shippment_charge = float(input())
        else:
            print('包邮')

        print("请输入竞品价格")
        Data.opponent_price = float(input())
        if int(Data.shippment_charge_judge) == 1:
            Data.opponent_price = Data.opponent_price + Data.shippment_charge


    def caculation(self):
        Data.product_price = ((Data.profit + Data.freight_charges + Data.china_price) / Data.exchange_rate) / 0.87
        Data.final_price = Data.product_price / 0.65
        airexpress_commission = Data.product_price * 0.08
        promotion_cost = Data.product_price * 0.05

        # print(product_price,final_price)

    def product_info(self):

        print("######商品信息######")
        print('商品名称：', Data.product_name)
        print('商品标题：', Data.product_title)
        print('重量:', Data.weight)
        print('货源地址：', Data.china_product_url)
        print("对手是否包邮：", Data.shippment_charge)

        print("#######平台抽成#######")
        print('平台佣金：美元$', Data.airexpress_commission)
        print('推广成本：美元$', Data.promotion_cost)
        print('\033[1;33m 仔细点 \" %s .\"\033[3;31m')

        print("#######价格信息#######")
        print('目标利润: 人民币￥', Data.profit)
        print("物流价格：人民币￥", Data.freight_charges)
        print('拿货价格：人民币￥', Data.china_price)
        print('折扣价格：美元$', Data.product_price)
        print('竞品价格：美元$', Data.opponent_price)
        print('输出价格：美元$', Data.final_price)

if __name__ == '__main__':
    t = 1
    t1 =1
    while t:
        d = Data()
        d.get_information()
        while t1:
            d.get_caculate_information()
            d.caculation()
            d.product_info()
        print('是否有变体且需要计算(0/1)：')
        t = int(input())


